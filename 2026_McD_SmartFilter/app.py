import streamlit as st
import openpyxl
from openpyxl.styles import Font, PatternFill
from io import BytesIO
from copy import copy

def get_data_dictionary(ws, target_headers):
    """Helper function to extract sheet data into a dictionary keyed by National Store #"""
    normalized_targets = {" ".join(h.lower().split()): h for h in target_headers}
    found_columns_map = {}
    
    # Locate columns
    for col_idx in range(1, ws.max_column + 1):
        cell_val = ws.cell(row=2, column=col_idx).value
        if not cell_val:
            cell_val = ws.cell(row=1, column=col_idx).value
            
        if cell_val:
            normalized_cell_text = " ".join(str(cell_val).lower().split())
            if normalized_cell_text in normalized_targets:
                # Store using the EXACT target header case to match our valid_columns logic later
                found_columns_map[normalized_targets[normalized_cell_text]] = col_idx
                
    if "National Store #" not in found_columns_map:
        return None, found_columns_map
        
    data_dict = {}
    # Extract row values
    for row in ws.iter_rows(min_row=3, values_only=True):
        nsn_col_index = found_columns_map["National Store #"] - 1 # 0-indexed for tuple
        if nsn_col_index >= len(row) or row[nsn_col_index] is None:
            continue
            
        nsn = str(row[nsn_col_index]).strip()
        row_data = {}
        for header in target_headers:
            if header in found_columns_map:
                val_idx = found_columns_map[header] - 1
                row_data[header] = str(row[val_idx]).strip() if val_idx < len(row) and row[val_idx] is not None else "N/A"
            else:
                row_data[header] = "N/A"
                
        data_dict[nsn] = row_data
        
    return data_dict, found_columns_map

def process_excel(file_prev, file_curr):
    # Load workbooks
    wb_prev = openpyxl.load_workbook(file_prev)
    wb_curr = openpyxl.load_workbook(file_curr)
    
    if "Field Contacts" not in wb_prev.sheetnames or "Field Contacts" not in wb_curr.sheetnames:
        st.error("Error: Both files must contain a tab named 'Field Contacts'.")
        return None
        
    ws_prev = wb_prev["Field Contacts"]
    ws_curr = wb_curr["Field Contacts"]
    
    target_headers = [
        "National Store #", "District", "PEOPLE PARTNERS", "LEX Supervisor", 
        "Risk", "Security", "VP", "Operations Officer", "Deployment Lead", 
        "Operations Manager", "Area Supervisor", "PC Ops Name"
    ]
    
    # 1. Extract Data Dictionaries for Comparison
    prev_data, _ = get_data_dictionary(ws_prev, target_headers)
    curr_data, curr_cols_map = get_data_dictionary(ws_curr, target_headers)
    
    if prev_data is None or curr_data is None:
        st.error("Error: 'National Store #' column not found in one or both files.")
        return None

    # --- COMPARISON LOGIC ---
    prev_nsns = set(prev_data.keys())
    curr_nsns = set(curr_data.keys())
    
    added_nsns = curr_nsns - prev_nsns
    removed_nsns = prev_nsns - curr_nsns
    common_nsns = curr_nsns.intersection(prev_nsns)
    
    changes_list = []
    
    # Check Added
    for nsn in added_nsns:
        pc = curr_data[nsn].get("PC Ops Name", "N/A")
        changes_list.append(["ADD", nsn, pc, "Store", "N/A", "New Store", "Yes"])
        
    # Check Changed
    for nsn in common_nsns:
        for col in target_headers:
            if col in ["National Store #", "District", "PC Ops Name"]:
                continue # Skip primary keys / identifiers for role change flags
                
            old_val = prev_data[nsn].get(col)
            new_val = curr_data[nsn].get(col)
            
            if old_val != new_val:
                pc = curr_data[nsn].get("PC Ops Name", "N/A")
                action = "Yes" # Default action flag, can be adjusted based on your business logic
                changes_list.append(["CHANGE", nsn, pc, col, old_val, new_val, action])

    # --- CREATE NEW WORKBOOK ---
    new_wb = openpyxl.Workbook()
    
    # TAB 1: SUMMARY
    ws_summary = new_wb.active
    ws_summary.title = "Summary"
    bold_font = Font(bold=True)
    
    ws_summary.append(["US McOpCo Roster Changes – Update"])
    ws_summary.cell(row=1, column=1).font = Font(bold=True, size=14)
    ws_summary.append([])
    
    ws_summary.append(["Key Highlights"])
    ws_summary.cell(row=3, column=1).font = bold_font
    ws_summary.append([f"✅ {len(added_nsns)} New Stores Added"])
    ws_summary.append([f"⚠️ {len(removed_nsns)} Store Removed"])
    ws_summary.append([f"🔄 {len([c for c in changes_list if c[0] == 'CHANGE'])} Role Changes"])
    ws_summary.append([])
    
    ws_summary.append(["Action Required Changes"])
    ws_summary.cell(row=8, column=1).font = bold_font
    summary_headers = ["Change Type", "NSN", "Profit Center", "Role", "Previous", "New", "Action"]
    ws_summary.append(summary_headers)
    for col_num in range(1, len(summary_headers) + 1):
        ws_summary.cell(row=9, column=col_num).font = bold_font
        ws_summary.cell(row=9, column=col_num).fill = PatternFill(start_color="EEEEEE", end_color="EEEEEE", fill_type="solid")
        
    for change in changes_list:
        ws_summary.append(change)
        
    ws_summary.append([])
    ws_summary.append(["Store Changes"])
    ws_summary.cell(row=ws_summary.max_row, column=1).font = bold_font
    
    ws_summary.append(["➕ Stores Added"])
    ws_summary.cell(row=ws_summary.max_row, column=1).font = bold_font
    for nsn in added_nsns:
        pc = curr_data[nsn].get('PC Ops Name', 'N/A')
        ws_summary.append([f"• NSN {nsn} – Profit Center {pc}"])
        
    ws_summary.append([])
    ws_summary.append(["➖ Stores Removed"])
    ws_summary.cell(row=ws_summary.max_row, column=1).font = bold_font
    for nsn in removed_nsns:
        pc = prev_data[nsn].get('PC Ops Name', 'N/A')
        ws_summary.append([f"• NSN {nsn} – Profit Center {pc}"])

    # TAB 2: CURRENT DATASET CHANGES (Original Red-Text Logic)
    ws_changes = new_wb.create_sheet("Current dataset changes")
    
    # 2. Reorder columns to strictly match your target_headers list
    valid_columns = []
    headers = []
    
    for target in target_headers:
        # We now look for the EXACT target string, since that is how we saved it in curr_cols_map
        if target in curr_cols_map:
            valid_columns.append(curr_cols_map[target])
            headers.append(target)
            
    ws_changes.append(headers)
    
    # 3. Find rows starting from row 3 in the CURRENT file
    for row in ws_curr.iter_rows(min_row=3):
        is_red_row = False
        
        # Check for red text ONLY within the valid columns
        for col_idx in valid_columns:
            cell = ws_curr.cell(row=row[0].row, column=col_idx)
            if cell.font and cell.font.color and cell.font.color.type == 'rgb':
                if cell.font.color.rgb in ['FF0000', 'FFFF0000']:
                    is_red_row = True
                    break
                    
        # 4. Extract the valid columns in the new exact order and preserve fonts
        if is_red_row:
            row_data = []
            cell_fonts = []
            
            for col_idx in valid_columns:
                source_cell = ws_curr.cell(row=row[0].row, column=col_idx)
                row_data.append(source_cell.value)
                cell_fonts.append(copy(source_cell.font) if source_cell.font else None)
                
            # Append the data to the new sheet
            ws_changes.append(row_data)
            
            # Apply the saved fonts to the newly added row
            new_row_idx = ws_changes.max_row
            for i, font in enumerate(cell_fonts):
                if font:
                    ws_changes.cell(row=new_row_idx, column=i + 1).font = font
            
    # Save the new workbook to an in-memory byte stream
    output = BytesIO()
    new_wb.save(output)
    output.seek(0)
    
    return output

# --- Web Interface (Streamlit) ---

st.set_page_config(page_title="Excel Contact Filter & Comparison", page_icon="📊", layout="wide")

st.title("Excel Contact Filter & Comparison")
st.write("Upload your **Previous** and **Current** McOpCo Alignment spreadsheets. The system will compare the two to generate a Summary of changes, and extract specific columns with **red text** from the current file.")

col1, col2 = st.columns(2)

with col1:
    file_previous = st.file_uploader("1️⃣ Upload PREVIOUS File (.xlsx)", type=["xlsx"])
    
with col2:
    file_current = st.file_uploader("2️⃣ Upload CURRENT File (.xlsx)", type=["xlsx"])

if file_previous is not None and file_current is not None:
    if st.button("Generate Comparison & Filter", type="primary"):
        with st.spinner("Analyzing changes and processing files..."):
            processed_file_stream = process_excel(file_previous, file_current)
            
        if processed_file_stream:
            st.success("Comparison complete! File processed successfully.")
            
            # Download button widget
            st.download_button(
                label="📥 Download Output File",
                data=processed_file_stream,
                file_name="Filtered_And_Compared_Contacts.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
