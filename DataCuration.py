import pandas as pd



predSNP=pd.read_csv("Deltapathogenicity.csv",sep='\t')
Chi_results=pd.read_csv("DeltaResults.tsv",sep='\t')
AAMut=pd.read_csv("AAMut.Delta.txt",sep='\t',header=None)
AAMut.columns=['Mutation','AA_Mutation']


#Count number of columns made after split.
colnum=len(AAMut['AA_Mutation'].str.split(',',expand=True).columns)
#Construct cols list
col_list=[]
for i in range(1,colnum+1):
    col_list.append("M"+str(i))
#Make n columns for split
AAMut[col_list] = AAMut['AA_Mutation'].str.split(',',expand=True)


#Merge on nt Mutation
df=pd.merge(Chi_results,AAMut,on=["Mutation"],how="left")



for i in col_list:
    #Combine columns in predSNP
    cols = ['Wild residue', 'Position', 'Target residue']
    predSNP[i] = predSNP[cols].apply(lambda row: ''.join(row.values.astype(str)), axis=1)        
    df=pd.merge(df,predSNP,on=[i],how="left")
    

if len(col_list) == 3:
    df=df[['Strain', 'Strain Total', 'Mutation','AA_Mutation','PredictSNP prediction_x', 'PredictSNP expected accuracy_x',
           'PhD-SNP prediction_x', 'PhD-SNP expected accuracy_x','PredictSNP prediction_y', 'PredictSNP expected accuracy_y',
           'PhD-SNP prediction_y', 'PhD-SNP expected accuracy_y','PredictSNP prediction', 'PredictSNP expected accuracy',
           'PhD-SNP prediction', 'PhD-SNP expected accuracy','Mutation Total', 'Has Mutation',
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
if len(col_list) == 2:
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
if len(col_list) == 1:
    df=df[['Strain', 'Strain Total', 'Mutation','AA_Mutation','PredictSNP prediction', 'PredictSNP expected accuracy',
           'PhD-SNP prediction', 'PhD-SNP expected accuracy','Mutation Total', 'Has Mutation',
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
