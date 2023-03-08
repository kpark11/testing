# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 20:56:28 2023

@author: brian
"""
import pandas as pd

file = r'C:\Users\brian\Downloads\TN1.recoded.csv'
file1 = r'C:\Users\brian\Downloads\ListofDups.csv'

df = pd.read_csv(file)
reference = pd.read_csv(file1)


new_df = df

df_dups = new_df[new_df.duplicated(subset=['patientIdNumber','Cancer'], keep=False)]
df_dups_reference = reference[reference.duplicated(subset=['patientIdNumber','Cancer'], keep=False)]

df_noDups = new_df.sort_values('dateOfDiagnosis').drop_duplicates(subset=['patientIdNumber','Cancer'], keep='first',ignore_index=False)
df_noDups.index.name = 'myindex'
df_noDups = df_noDups.sort_values('myindex')
        
df_noDups.to_csv('noDups_TN1.recoded.csv')
