from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "G:\Software\Github\Data"
git_dir = "G:\Software\Github\BigData"
csv_file = "sample_data_clean.csv" 

# FOR LOOPS ---------------------------------
df = pd.read_csv(os.path.join(main_dir, csv_file))
list1 = range(10,15)
list2 = ['a','b','c']
list3 = [1,'a',True]

## iterating over elements (for loops)
for v in list1: # 'v' can be anything set as a reference
    v
    
for v in list2:
    print(v)
    
for sweet in list3:
    print(sweet,type(sweet), 'haha')
    
## populating empty lists
list1 # is all int
list4 = [] # empty list
list5 = []
for v in list1:
    v2 = v**2
    list4.extend([v2]) # extend only accepts 'list' object
    list5.append(v2) #appends whatever object as is
    
[v for v in list1]
[v**2 for v in list1]
list6 = [ v**2 < 144 for v in list1]


## iterating using enumerate
list7 = [ [i,v/2] for i, v in enumerate(list1)] #"enumerate" always pairs up an index and a value
list7 = [ [i,float(v)/2] for i, v in enumerate(list1)] 


# ITERATE RHTOUGH A SERIES -----------------------------
s1 = df['consump']
[v > 2 for v in s1]
[[i,float(v)*.3] for i, v in s1.iteritems()]


# ITERATE THROUGH A DATAFRAME ------------------------------
[v for v in df] # v represents the column key in df
[df[v] for v in df]
[[i,v] for i,v in df.iteritems()]
