# ---modulate imports---
import pandas as pd
#import re
# ---CSV file import---
df = pd.read_csv("/Users/jamie/Desktop/UNC Work Files/GU_TB_LIST_0211.csv")

# ---Column splits---
pat = df.iloc[:, 0].str.split('\n', expand=True)
pat.columns = ['PATIENT_name', 'PID', 'pAGE']

md = df.iloc[:, 1].str.split('\n', expand=True)
md.columns = ['MD', 'MD2', 'MD3', 'MD4', 'MD5', 'MD6']

refmd = df.iloc[:, 2].str.split('\n', expand=True)
refmd.column = ['refmd', 'refmd2']

diag = df.iloc[:, 3]

# ---replacement variables for to simplify diag---
p = 'Prostate'
b = 'Bladder'
t = 'Testicular'
w = 'Penile'
k = 'Renal'
u = 'Ureteral'
kid = 'Kidney'
o = 'Other'
u = 'Urothelial'
up = 'Upper Tract'
ur = 'Ureteral'
s = 'Scrotal'
cancer = [p,b,t,w,k,u,kid,o,u,up,ur,s]

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
    else:
        diag_type.append(string)
diag_sum = pd.DataFrame(diag_type)
diag_sum.columns = ['Cancer_Type']
print(diag_sum)

#print(diag_type)
#print(diag[0:30])


# ---Patient duplicate search---

#pid = pat[1]
#checklist = []
#for p_id in pid:
#    if p_id in checklist:
#        checklist.append(p_id)
#print (checklist)

# ---Dataframe Output---
df_out =  pd.concat([pat, md, refmd, diag_sum], axis=1, join_axes=[pat.index])
df_out.to_csv("/Users/jamie/Desktop/UNC Work Files/GU_TB_LIST_0211_export.csv", encoding='utf-8')

        