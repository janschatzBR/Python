import streamlit as st
import openpyxl
from io import BytesIO

def process_excel(uploaded_file):
    # Load the workbook from the uploaded file
    wb = openpyxl.load_workbook(uploaded_file)
    
    if "Field Contacts" not in wb.sheetnames:
        st.error("Error: A tab named 'Field Contacts' was not found in the uploaded file.")
        return None
        
    ws = wb["Field Contacts"]
    
    # Create a new workbook for the output
    new_wb = openpyxl.Workbook()
    new_ws = new_wb.active
    new_ws.title = "Field Contacts"
    
    yellow_columns = []
    headers = []
    
    # 1. Find columns with yellow headers
    for cell in ws[1]:
        if cell.fill and cell.fill.fgColor and cell.fill.fgColor.type == 'rgb':
            if cell.fill.fgColor.rgb in ['FFFF00', 'FFFFFF00']:
                yellow_columns.append(cell.column)
                headers.append(cell.value)
                
    if not yellow_columns:
        st.warning("No yellow headers found. Please check if a custom shade of yellow is being used.")
        return None
        
    new_ws.append(headers)
    
    # 2. Find rows with red text
    for row in ws.iter_rows(min_row=2):
        is_red_row = False
        
        for cell in row:
            if cell.font and cell.font.color and cell.font.color.type == 'rgb':
                if cell.font.color.rgb in ['FF0000', 'FFFF0000']:
                    is_red_row = True
                    break
                    
        # 3. Extract only the valid columns for that row
        if is_red_row:
            row_data = []
            for col_idx in yellow_columns:
                row_data.append(ws.cell(row=row[0].row, column=col_idx).value)
            new_ws.append(row_data)
            
    # Save the new workbook to an in-memory byte stream
    output = BytesIO()
    new_wb.save(output)
    output.seek(0)
    
    return output

# --- Web Interface (Streamlit) ---

st.set_page_config(page_title="Excel Color Filter", page_icon="📊")

st.title("Excel Color Filter")
st.write("Upload your spreadsheet. The system will extract rows with **red text**, keeping only the columns with **yellow headers** from the 'Field Contacts' tab.")

# File uploader widget
uploaded_file = st.file_uploader("Upload an Excel file (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    with st.spinner("Processing your file..."):
        processed_file_stream = process_excel(uploaded_file)
        
    if processed_file_stream:
        st.success("File processed successfully!")
        
        # Download button widget
        st.download_button(
            label="Download Filtered Contacts",
            data=processed_file_stream,
            file_name="Filtered_Field_Contacts.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
