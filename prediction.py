# create plot
import pandas as pd
import numpy as np
import joblib


df1=pd.read_csv('archive/Symptom-severity.csv')
discrp=pd.read_csv('archive/symptom_Description.csv')
ektra7at=pd.read_csv('archive/symptom_precaution.csv')

rnd_forest=joblib.load('random_forest.joblib')
def predd(x,S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16,S17):
    psymptoms = [S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16,S17]
    print(psymptoms)
    a = np.array(df1["Symptom"])
    b = np.array(df1["weight"])
    print(len(psymptoms),len(a))
    
    for j in range(len(psymptoms)):
        for k in range(len(a)):
            if psymptoms[j]==a[k]:
                psymptoms[j]=b[k]
    psy = [psymptoms]
    print('psy:',psy)
    pred2 = x.predict(psy)
    disp= discrp[discrp['Disease']==pred2[0]]
    disp = disp.values[0][1]
    recomnd = ektra7at[ektra7at['Disease']==pred2[0]]
    c=np.where(ektra7at['Disease']==pred2[0])[0][0]
    precuation_list=[]
    for i in range(1,len(ektra7at.iloc[c])):
          precuation_list.append(ektra7at.iloc[c,i])
    return pred2[0],disp,precuation_list

# symptom1=input('enter symptom1')
# symptom2=input('enter symptom2')
# symptom3=input('enter symptom3')

sympList=df1["Symptom"].to_list()
# print(sympList)
# predd(rnd_forest,symptom1,symptom2,symptom3,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
