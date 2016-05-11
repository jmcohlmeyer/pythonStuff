# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 21:15:17 2016

@author: jamie
"""

# ---modulate imports---
import pandas as pd
#import re
# ---CSV file import---
df = pd.read_csv("/Users/jamie/Desktop/UNC Work Files/tumorboarddata-5-1-16.csv")

# ---Column splits---
pat = df.iloc[:, 0].str.split('\n', expand=True)
pat.columns = ['PATIENT_name', 'PID', 'pAGE']

#print (pat)

md = df.iloc[:, 1].str.split('\n', expand=True)
md.columns = ['MD', 'MD2', 'MD3', 'MD4', 'MD5','MD6','MD7']

#print (md)

refmd = df.iloc[:, 2].str.split(',', expand=True)
refmd.columns = ['refmd-last','refmd-first', 'refmd-extra']

#print (refmd)

diag = df.iloc[:, 3]
p = 'Prostate'
b = 'Bladder'
t = 'Testicular'
w = 'Penile'
k = 'Renal'
u = 'Ureteral'
kid = 'Kidney'
o = 'Other'
uro = 'Urothelial'
up = 'Upper Tract'
ur = 'Ureteral'
s = 'Scrotal'
ure = 'Ureter'

cancer = [p,b,t,w,k,u,kid,o,uro,up,ur,s,ure]

# ---Loop for diag simplifcation---
diag_type = []
cnt = len(diag)
for string in diag:
    if cancer[0] in string:
        diag_type.append(cancer[0])
    elif cancer[1] in string:
        diag_type.append(cancer[1])
    elif cancer[2] in string:
        diag_type.append(cancer[2])
    elif cancer[3] in string:
        diag_type.append(cancer[3])
    elif cancer[4] in string:
        diag_type.append(cancer[6])
    elif cancer[5] in string:
        diag_type.append(cancer[5])
    elif cancer[6] in string:
        diag_type.append(cancer[6])
    elif cancer[7] in string:
        diag_type.append(cancer[7])
    elif cancer[8] in string:
        diag_type.append(cancer[9])        
    elif cancer[10] in string:
        diag_type.append(cancer[9])   
    elif cancer[11] in string:
        diag_type.append(cancer[2]) 
    elif cancer[12] in string:
        diag_type.append(cancer[9]) 
    else:
        diag_type.append(string)
diag_sum = pd.DataFrame(diag_type)
diag_sum.columns = ['Cancer_Type']
#print(diag_sum)

# ---Export reduced data as CSV---
df_out =  pd.concat([pat, md, refmd, diag_sum], axis=1, join_axes=[pat.index])
df_out.to_csv("/Users/jamie/Desktop/UNC Work Files/tumorboarddata-5-1-16export.csv", encoding='utf-8')

        
