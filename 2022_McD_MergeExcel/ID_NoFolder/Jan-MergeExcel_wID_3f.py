# merge 3 excel files in a folder by a common column

import pandas as pd

df1 = pd.read_excel("file1.xlsx")
df2 = pd.read_excel("file2.xlsx")
df3 = pd.read_excel("file3.xlsx")

#df_combine = df1.merge(df2, left_on="ID", right_on="project", how="outer")
merged = df1.merge(df2, on="ID", how="outer")
merged = merged.merge(df3, on="ID", how="outer")


merged.to_excel("merged_withID_3files.xlsx")
