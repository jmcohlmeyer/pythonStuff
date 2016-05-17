# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 21:15:17 2016

@author: jamie
"""

# ---modulate imports---
import pandas as pd
#import datetime as dt

#import re
# ---CSV file import---
#df1 = pd.read_csv("/Users/jamie/Desktop/UNC Work Files/ReferralandMailComboList.csv")
#headers  = list(df1)
#print(df1.head())


df = pd.read_csv("/Users/jamie/Desktop/UNC Work Files/GUConferencePrint-1532016.csv")

# ---Column splits---
pat = df.iloc[:, 0].str.split('\n', expand=True)
pat.columns = ['PATIENT_name', 'PID', 'pAGE']

#print (pat)

#md = df.iloc[:, 1].str.split('\n', expand=True)
#md.columns = ['MD', 'MD2', 'MD3', 'MD4', 'MD5','MD6']

# --- loop for referral date cleaning ----
referral_d = df.iloc[:,1]


#fmts = ('%m/%d/%Y','%m/%d/%y')
#
#parsed=[]
#for e in referral_d.splitlines():
#    for fmt in fmts:
#        try:
#           t = dt.datetime.strptime(e, fmt)
#           parsed.append((e, fmt, t)) 
#           break
#        except ValueError as err:
#           pass
#
## check that all the cases are handled        
#success={t[0] for t in parsed}
#for e in referral_d.splitlines():
#    if e not in success:
#        print (e)    
#
#for t in parsed:
#    print ('"{:20}" => "{:20}" => {}'.format(*t))
#
#



ref_date = []

#cnt = len(referral_d)

for d in referral_d:   
        ref_date.append('05/09/2016')
        
ref_date_sum = pd.DataFrame(ref_date)
ref_date_sum.columns = ['Referral Date']    
print (ref_date_sum)

refmd = df.iloc[:, 2].str.split(',', expand=True)
refmd.columns = ['Physician Last Name','Physician First Name']

#print (refmd)

diag = df.iloc[:, 3]
cancer = ['Prostate','Bladder','Testicular','Penile','Renal','Ureteral','Kidney','Other','Urothelial','Upper Tract','Ureteral','Scrotal','Ureter','Testis','Penis']

# ---Loop for diag simplifcation---
diag_type = []

for string in diag:
    if cancer[0] in string:
        diag_type.append(cancer[0])
    elif cancer[1] in string:
        diag_type.append(cancer[1])
    elif cancer[2] in string:
        diag_type.append(cancer[13])
    elif cancer[3] in string:
        diag_type.append(cancer[14])
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
    elif cancer[13] in string:
        diag_type.append(cancer[13]) 
    elif cancer[14] in string:
        diag_type.append(cancer[14]) 
    else:
        diag_type.append(string)
        
diag_sum = pd.DataFrame(diag_type)
diag_sum.columns = ['Cancer Type']
#print(diag_sum)


# --- Additional Variables to Export ---
#year = 2016

# ---Export reduced data as CSV---
df_out =  pd.concat([ref_date_sum, diag_sum, refmd], axis=1, join_axes=[pat.index])
df_out.to_csv("/Users/jamie/Desktop/UNC Work Files/test-05122016.csv", encoding='utf-8')

        
