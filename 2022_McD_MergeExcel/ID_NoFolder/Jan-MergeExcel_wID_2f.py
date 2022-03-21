# merge 2 excel files in a folder by a common column

import pandas as pd

df1 = pd.read_excel("file1.xlsx")
df2 = pd.read_excel("file2.xlsx")

merged = df1.merge(df2, on="ID", how="outer")

merged.to_excel("merged_withID_2files.xlsx")
