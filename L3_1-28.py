from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "G:\Software\Github\Data"
git_dir = "G:\Software\Github\BigData"
csv_file_os = "sample_data_clean.csv" # use when using os
csv_file_path = "\sample_data_clean.csv" # use when using direct path

# os module (another way for pathing)-----------------------------
df_os = pd.read_csv(os.path.join(main_dir, csv_file_os))
df_path = pd.read_csv(main_dir + csv_file_path)

# Python data types --------------------------

## Strings
str1 = "hello, computer" # Type str
str2 = 'hello, human' # Type str, string can be in double or single quote
str3 = u'eep' # unicode, can be used in all systems and programs 

type(str1)
type(str2)
type(str3)

## numeric
int1 = 10
float1 = 20.45
long1 = 34598695048687890989999

## logical
bool1= True
notbool1 = 0
bool2 = bool(notbool1)

#  Creating LIsts and tuples ---------------------------

## in brief, lists can be changed, tuples cannot 
## we almost exclusively use lists

list1 = []
list1
list2 = [5, 4, 'a']
list2[2] # output 'a', python counts from 0.
list2[2] = 5

## tup;es, cant change
tup1 = (8,3,19)
tup1[2] #outputs is 19
tup1[2] = 5 #tuples does not support assignment

## convert
list2 = list(tup1) # convert tuple to list
tup2 = tuple(list1) # convert list to tuple
list2[2]

## list can be append and extended
list2 = [8, 3, 19]
list2.append([3, 90])  # out: [8, 3, 19, [3, 90]]
len(list2)
list3 = [8, 3, 90]
list3.extend([6, 88]) # out: [8, 3, 90, 6, 88]
len(list3)


#  CONVERTING LISTS TO SERIES AND DATAFRAME
list4 = range(100,105) # range(n,m) -- gives a list from # n to m-1
list5 = range(5) #F range(m) -- gives list from 0 to m-1
list5 # [0, 1, 2, 3, 4]
list6 = ['q', 'r', 's', 't', 'u']

## list to series
s1 = Series(list4)
s2 = Series(list5)
s3 = Series(list6)

## lists to DataFrame


