from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# IMPORTING DATA  --------------------------------------------------

## assigning file paths
main_dir = "G:\Software\Github\BigData\live_memo"
csv_file = "\data\sample_data_clean.csv"
txt_file = "\data\sample_data_clean.txt"

main_dir + csv_file
main_dir + txt_file

# read_csv and read_table
df = pd.read_csv(main_dir + csv_file)
df2 = pd.read_table(main_dir + txt_file) 

## check object type
type(df)
type(df2)

# EXPLORING DATAFRAME  ---------------------------------------------

list(df) # quick way to get the names of dataframe
list(df2)

## extracting columns data (Series)
c = df.consump # extract the data as a series
c2 = df['consump']

type(c)


## BOOLEAN (LOGICAL) OPERATORS ------------------------------------
### boolean comparison, have to use two equal signs, one means assigning
c == c2 #test equality
c > c2 #test greater than
c >= c2
c != c2
# other boolean operators are <, <=, !=(not equal to)


# ROW EXTRACTION -------------------------------------------------

## method 1:row slicing
df[5:10] # df[m:n] yields rows m to n-1
df[0:10]
df[:10]
df[0:10] == df[:10]
df[10:11] # get row 10


## row slicing from series
c[5:10]
df.consump[5:10]

## extraction by boolean indexing
df.panid == 4
df[df.panid == 4] # extract subset of df where panid == 4
df[df.consump > 2]
df.panid[df.panid > 2]


