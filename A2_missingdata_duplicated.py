from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "G:\Software\Github\Data"
git_dir = "G:\Software\Github\BigData"
csv_file = "small_data_w_missing_duplicated.csv"

df = pd.read_csv(os.path.join(main_dir, csv_file))
df.isnull()

# 1. CONVERT MISSING DATA TO NaN VALUES-----------------------------------------
missing = ['.','','NA','NULL','-']
df = pd.read_csv(os.path.join(main_dir,csv_file), na_values = missing)

# 2. DROP FULL ROWS THAT ARE DUPLICATED ----------------------------------------
df1 = df.drop_duplicates()

# 3. EXTRACT FULL ROWS OF DATA WHERE 'CONSUMP' HAS MISSING VALUES---------------
rows = df1['consump'].isnull()
df1[rows]

# 4. Check for any duplicated values on the SUBSET of panid and date. Drop the 
#    rows where consump is missing for any duplicated values
t_b = df1.duplicated(['panid','date'])
b_t = df1.duplicated(['panid','date'],take_last = True)
na = df1['consump'].isnull()
dup_na = ~((t_b|b_t)&na)
df2 = df1[dup_na]

# 5 Average of cleaned data
ave = df2.consump.mean()