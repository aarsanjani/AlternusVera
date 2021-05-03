import pandas as pd
import numpy as np
import csv

myfile = open('Social_Network_Ads_Enriched.csv','a+', encoding='utf-8')
wrtr = csv.writer(myfile, delimiter='\t', quotechar='"')

df1=pd.read_csv("kag1.csv")
df2=pd.read_csv("sn1.csv")

df1['min_age'], df1['max_age'] = df1['age'].str.split('-', 3).str

df2.loc[df2['Gender'] =="Male", 'Gender'] = "M"
df2.loc[df2['Gender'] =="Female", 'Gender'] = "F"

df1.min_age = pd.to_numeric(df1.min_age, errors='coerce')
df1.max_age = pd.to_numeric(df1.max_age, errors='coerce')

df1.drop(['age'],axis=1, inplace=True)


for index, row in df2.iterrows():
    df3= df1.loc[(df1['gender'] == row['Gender'] & row['Age']>= df1['min_age'] & row['Age'] <= df1['min_age'] & row['Purchased'] == df1['Approved_Conversion'])]
    csvRow=[row.iloc[index], df3.iloc[0]]
	wrtr.writerow(csvRow)
    myfile.flush()
	
myfile.close()