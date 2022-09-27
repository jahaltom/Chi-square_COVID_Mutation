import pandas as pd



predSNP=pd.read_csv("Deltapathogenicity.csv",sep='\t')
Chi_results=pd.read_csv("DeltaResults.tsv",sep='\t')
data=pd.read_csv("DeltaDataWithKeywords.tsv",sep='\t')[['Mutations', 'substitutions']]
data = data.rename(columns={'Mutations': 'Mutation'}).drop_duplicates()
Chi_results=pd.merge(Chi_results,data,on=["Mutation"],how="left")







AAMut=pd.read_csv("AAMut.Delta.txt",sep='\t',header=None)
AAMut.columns=['substitutions','AA_Mutation']


#Count number of columns made after split.
colnum=len(AAMut['AA_Mutation'].str.split(',',expand=True).columns)
#Construct cols list
col_list=[]
for i in range(1,colnum+1):
    col_list.append("M"+str(i))
#Make n columns for split
AAMut[col_list] = AAMut['AA_Mutation'].str.split(',',expand=True)


#Merge on nt Mutation
df=pd.merge(Chi_results,AAMut,on=["substitutions"],how="left")



for i in col_list:
    #Combine columns in predSNP
    cols = ['Wild residue', 'Position', 'Target residue']
    predSNP[i] = predSNP[cols].apply(lambda row: ''.join(row.values.astype(str)), axis=1)        
    df=pd.merge(df,predSNP,on=[i],how="left")
    

if len(col_list) == 3:
    df=df[['Strain', 'Strain Total', 'Mutation','AA_Mutation','PredictSNP prediction_x', 'PredictSNP expected accuracy_x',
           'PhD-SNP prediction_x', 'PhD-SNP expected accuracy_x','PredictSNP prediction_y', 'PredictSNP expected accuracy_y',
           'PhD-SNP prediction_y', 'PhD-SNP expected accuracy_y','PredictSNP prediction', 'PredictSNP expected accuracy',
           'PhD-SNP prediction', 'PhD-SNP expected accuracy']
          +Chi_results.iloc[: , df.columns.get_loc('Mutation Total'):].columns.values.tolist()]
    
if len(col_list) == 2:
    df=df[['Strain', 'Strain Total', 'Mutation','AA_Mutation','PredictSNP prediction_x', 'PredictSNP expected accuracy_x',
           'PhD-SNP prediction_x', 'PhD-SNP expected accuracy_x','PredictSNP prediction_y', 'PredictSNP expected accuracy_y',
           'PhD-SNP prediction_y', 'PhD-SNP expected accuracy_y']
          +Chi_results.iloc[: , df.columns.get_loc('Mutation Total'):].columns.values.tolist()]
    
if len(col_list) == 1:
    df=df[['Strain', 'Strain Total', 'Mutation','AA_Mutation','PredictSNP prediction', 'PredictSNP expected accuracy','PhD-SNP prediction', 'PhD-SNP expected accuracy']
          +Chi_results.iloc[: , df.columns.get_loc('Mutation Total'):].columns.values.tolist()]


df.to_csv("Delta_Final_Results.tsv",sep='\t',index=False,mode='w')
