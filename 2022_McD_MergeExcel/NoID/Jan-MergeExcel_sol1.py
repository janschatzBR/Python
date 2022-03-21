# merge all excel files in a folder

# importing libraries
import os
import pandas as pd

# getting current working directory and files within it
# cwd shows the path to the current working directory
# files is a list of all the file names within the current working directory
cwd = os.path.abspath('')
files = os.listdir(cwd)  

## Method 1 gets the first sheet of a given file

# dataframe df for storing the data for master spreadsheet. We loop through all the files within the current working directory, but only process the Excel files whose name ends with “.xlsx” or ".xls"
# pd.read_excel() will read Excel data into Python and store it as a pandas DataFrame object. Be aware that this method reads only the first tab/sheet of the Excel file by default
# df.append() will append/combine data from one file to another. Data is stored inside your computer’s memory.
# df.head() shows the first 5 rows of the data, to examine the master dataframe
# df.to_excel output the data back into Excel
df = pd.DataFrame()

for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel(file), ignore_index=True)
        
df.head()
df.to_excel('merged_onesheet_withoutID1.xlsx')

### ###

## Method 2 gets all sheets of a given file

df_total = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'): #or file.endswith('.xls'):
        excel_file = pd.ExcelFile(file)
        sheets = excel_file.sheet_names
        for sheet in sheets:               # loop through sheets inside an Excel file
            df = excel_file.parse(sheet_name = sheet)
            df_total = df_total.append(df)
df_total.to_excel('merged_allsheet_withoutID1.xlsx')
