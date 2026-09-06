import pandas as pd
import numpy as np
df=pd.read_csv('C:/Users/DELL/OneDrive/Bureau/Abderazak_Portfolio/WA_Fn-UseC_-Telco-Customer-Churn.csv')
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width', None)
print(df.head(5))
print(df.info())
#print(df.describe(include='all').T)
#print(df.nunique())
df.columns=df.columns.str.strip().str.replace(" ", "_").str.lower()
df['totalcharges']=pd.to_numeric(df['totalcharges'], errors='coerce')
print(df.isnull().sum())
print(df.shape)
cols=['customerid', 'gender', 'partner', 'dependents',
       'phoneservice', 'multiplelines', 'internetservice',
       'onlinesecurity', 'onlinebackup', 'deviceprotection', 'techsupport',
       'streamingtv', 'streamingmovies', 'contract', 'paperlessbilling',
       'paymentmethod', 'totalcharges', 'churn']
for col in cols:
    df[col]=df[col].astype(str).str.strip().str.lower()
    df[col]=df[col].replace({'nan':np.nan})
    df[col]=df[col].str.title()
print(df)
df.to_csv('C:/Users/DELL/OneDrive/Bureau/Abderazak_Portfolio/Telco_Clean.csv', index=False)
