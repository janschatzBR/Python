# merge all excel files in a folder

import pandas as pd
import glob

# getting excel files to be merged 
path = "C:\\PyJan\\"

# read all the files with extension .xlsx i.e. excel 
filenames = glob.glob(path + "\*.xlsx")
print('File names:', filenames)

# empty data frame for the new output excel file with the merged excel files
outputxlsx = pd.DataFrame()

# for loop to iterate all excel files
for file in filenames:
   # using concat for excel files
   # after reading them with read_excel()
   df = pd.concat(pd.read_excel( file, sheet_name=None), ignore_index=True, sort=False)

   # appending data of excel files
   outputxlsx = outputxlsx.append( df, ignore_index=True)

print('Final Excel sheet now generated at the same location:')
outputxlsx.to_excel("merged_withoutid_2.xlsx", index=False)
