# merge 3 excel files in a folder by a common column

import pandas as pd
import glob

import os

import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore") #for Data validation (not supported by openpyxl)

files1 = os.listdir('C:/PyJan/Dev/File1/')
filtered_files = [file_  for file_ in files1 if file_.endswith('.xlsx')]
df1 = pd.read_excel('C:/PyJan/Dev/File1'+'/'+filtered_files[0])
print(df1.head())
print("FILE 1 READ\n")

files2 = os.listdir('C:/PyJan/Dev/File2/')
filtered_files = [file_  for file_ in files2 if file_.endswith('.xlsx')]
df2 = pd.read_excel('C:/PyJan/Dev/File2'+'/'+filtered_files[0])
print(df2.head())
print("FILE 2 READ\n")

files3 = os.listdir('C:/PyJan/Dev/File3/')
filtered_files = [file_  for file_ in files3 if file_.endswith('.xls')]
df3 = pd.read_excel('C:/PyJan/Dev/File3'+'/'+filtered_files[0])
print(df3.head())
print("FILE 3 READ\n")

#df_combine = df1.merge(df2, left_on="ID", right_on="project", how="outer")
merged = df1.merge(df2, on="ID", how="outer")
merged = merged.merge(df3, on="ID", how="outer")
print(merged.head())
merged.to_excel("merged_withID_3files.xlsx")
print("\nMERGED FILE CREATED")
