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
df.drop_duplicates()
df.drop_duplicates(take_last = True)
t_b = df.duplicated()
df[~t_b]

# 3. EXTRACT FULL ROWS OF DATA WHERE 'CONSUMP' HAS MISSING VALUES---------------
rows = df['consump'].isnull()
df[rows]

# 4. 