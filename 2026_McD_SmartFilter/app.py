import streamlit as st
import openpyxl
from io import BytesIO
from copy import copy

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
    
    # This list now dictates the EXACT order of columns in the output file
    target_headers = [
        "National Store #", "District", "PEOPLE PARTNERS", "LEX Supervisor", 
        "Risk", "Security", "VP", "Operations Officer", "Deployment Lead", 
        "Operations Manager", "Area Supervisor", "PC Ops Name"
    ]
    
    # Normalize targets to handle slight text variations
    normalized_targets = {" ".join(h.lower().split()): h for h in target_headers}
    
    # Temporary dictionary to map found headers to their original column index
    found_columns_map = {}
    
    # 1. Scan the source sheet to find where each target column lives
    for col_idx in range(1, ws.max_column + 1):
        cell_val = ws.cell(row=2, column=col_idx).value
        if not cell_val:
            cell_val = ws.cell(row=1, column=col_idx).value
            
        if cell_val:
            normalized_cell_text = " ".join(str(cell_val).lower().split())
            if normalized_cell_text in normalized_targets:
                found_columns_map[normalized_cell_text] = col_idx
                
    # 2. Reorder columns to strictly match your target_headers list
    valid_columns = []
    headers = []
    
    for target in target_headers:
        normalized_target = " ".join(target.lower().split())
        if normalized_target in found_columns_map:
            valid_columns.append(found_columns_map[normalized_target])
            headers.append(target)
            
    if not valid_columns:
        st.warning("None of the specified headers were found.")
        return None
        
    new_ws.append(headers)
    
    # 3. Find rows starting from row 3
    for row in ws.iter_rows(min_row=3):
        is_red_row = False
        
        # Check for red text ONLY within the valid columns
        for col_idx in valid_columns:
            cell = ws.cell(row=row[0].row, column=col_idx)
            if cell.font and cell.font.color and cell.font.color.type == 'rgb':
                if cell.font.color.rgb in ['FF0000', 'FFFF0000']:
                    is_red_row = True
                    break
                    
        # 4. Extract the valid columns in the new exact order and preserve fonts
        if is_red_row:
            row_data = []
            cell_fonts = []
            
            for col_idx in valid_columns:
                source_cell = ws.cell(row=row[0].row, column=col_idx)
                row_data.append(source_cell.value)
                
                cell_fonts.append(copy(source_cell.font) if source_cell.font else None)
                
            # Append the data to the new sheet
            new_ws.append(row_data)
            
            # Apply the saved fonts to the newly added row
            new_row_idx = new_ws.max_row
            for i, font in enumerate(cell_fonts):
                if font:
                    new_ws.cell(row=new_row_idx, column=i + 1).font = font
            
    # Save the new workbook to an in-memory byte stream
    output = BytesIO()
    new_wb.save(output)
    output.seek(0)
    
    return output

# --- Web Interface (Streamlit) ---

st.set_page_config(page_title="Excel Contact Filter", page_icon="📊")

st.title("Excel Contact Filter")
st.write("Upload your spreadsheet. The system will extract specific columns in a **fixed order** (starting with National Store), but **only if** one of those columns contains **red text**. Original text colors will be preserved.")

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
