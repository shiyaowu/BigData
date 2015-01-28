from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# IMPORT DATA ------------------------------------------------------
main_dir = "G:\Software\Github\BigData\A1"
txt_file = "\File1_small.txt"
main_dir + txt_file
df = pd.read_table(main_dir + txt_file, sep = ' ') 
# read txt file which uses space as seperator 

# DATA EXTRACTION --------------------------------------------------
df[60:100] # extract rows 60 to 99 of the dataframe
list(df) # get the names of the dataframe
df[df.kwh > 30] # extract rows where kwh is greater than 30

