import pandas as pd



predSNP=pd.read_csv("Deltapathogenicity.csv",sep='\t')
Chi_results=pd.read_csv("DeltaResults.tsv",sep='\t')
AAMut=pd.read_csv("AAMut.Delta.txt",sep='\t',header=None)
AAMut.columns=['Mutation','AA_Mutation']




#Count number of columns made after split. 
len(AAMut['AA_Mutation'].str.split(',',expand=True).columns)

#Make 2 columns for split 
AAMut[['M1','M2']] = AAMut['AA_Mutation'].str.split(',',expand=True)




#Combine columns in predSNP
cols = ['Wild residue', 'Position', 'Target residue']
predSNP['M1'] = predSNP[cols].apply(lambda row: ''.join(row.values.astype(str)), axis=1)



#Merge on nt Mutation
df=pd.merge(Chi_results,AAMut,on=["Mutation"],how="left")



df=pd.merge(df,predSNP,on=["M1"],how="left")

#Combine columns in predSNP
cols = ['Wild residue', 'Position', 'Target residue']
predSNP['M2'] = predSNP[cols].apply(lambda row: ''.join(row.values.astype(str)), axis=1)


df=pd.merge(df,predSNP,on=["M2"],how="left")





df=df[['Strain', 'Strain Total', 'Mutation','AA_Mutation','PredictSNP prediction_x', 'PredictSNP expected accuracy_x',
       'PhD-SNP prediction_x', 'PhD-SNP expected accuracy_x','PredictSNP prediction_y', 'PredictSNP expected accuracy_y',
       'PhD-SNP prediction_y', 'PhD-SNP expected accuracy_y','Mutation Total', 'Has Mutation',
       'Very-Mild_Asymptomatic', 'Mild', 'Moderate', 'Very_Severe', 'Dead',
       'Mild vs Moderate P-value', 'Mild vs Moderate Severity Correlation',
       'Moderate vs Dead P-value', 'Moderate vs Dead Severity Correlation',
       'Dead vs All', 'Mild vs Dead P-value',
       'Mild vs Dead Severity Correlation', 'Very_Severe vs Mild P-value',
       'Very_Severe vs Mild Severity Correlation',
       'Very-Mild_Asymptomatic vs Dead P-value',
       'Very-Mild_Asymptomatic vs Dead Severity Correlation',
       'Very_Severe vs Dead P-value',
       'Very_Severe vs Dead Severity Correlation',
       'Very_Severe vs Very-Mild_Asymptomatic P-value',
       'Very_Severe vs Very-Mild_Asymptomatic Severity Correlation']]


df.to_csv("Delta_Final_Results.tsv",sep='\t',index=False,mode='w')
