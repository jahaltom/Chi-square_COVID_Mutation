import os
import pandas as pd
from scipy.stats import chi2_contingency


os.chdir(r"C:\Users\15154\Desktop\OFR10_Nidia\scripts")


#Make all keywords lowercase in text files and remake files as tsv. 
with open ("Dead.tsv") as f:
        dead_list=f.read().splitlines()
        temp=[x.lower() for x in dead_list]
        dead_list=temp
        dead_df=pd.DataFrame(dead_list).drop_duplicates()
        dead_df.to_csv("Dead.tsv",sep='\t',mode='w',index=None,header=None)
        
with open ("Mild.tsv") as f:
        mild_list=f.read().splitlines()
        temp=[x.lower() for x in mild_list]
        mild_list=temp
        mild_df=pd.DataFrame(mild_list).drop_duplicates()
        mild_df.to_csv("Mild.tsv",sep='\t',mode='w',index=None,header=None)
          
        
with open ("Moderate.tsv") as f:
        moderate_list=f.read().splitlines()
        temp=[x.lower() for x in moderate_list]
        moderate_list=temp
        moderate_df=pd.DataFrame(moderate_list).drop_duplicates()
        moderate_df.to_csv("Moderate.tsv",sep='\t',mode='w',index=None,header=None)
    
with open ("Very_Severe.tsv") as f:
        very_severe_list=f.read().splitlines()
        temp=[x.lower() for x in very_severe_list]
        very_severe_list=temp
        very_severe_df=pd.DataFrame(very_severe_list).drop_duplicates()
        very_severe_df.to_csv("Very_Severe.tsv",sep='\t',mode='w',index=None,header=None)

        
with open ("VeryMild_Asymptomatic.tsv") as f:
        veryMild_asymptomatic_list=f.read().splitlines()
        temp=[x.lower() for x in veryMild_asymptomatic_list]
        veryMild_asymptomatic_list=temp
        veryMild_asymptomatic_df=pd.DataFrame(veryMild_asymptomatic_list).drop_duplicates()
        veryMild_asymptomatic_df.to_csv("VeryMild_Asymptomatic.tsv",sep='\t',mode='w',index=None,header=None)

 
        
#Some pateints will be excluded becuase they failed to have a status keyword. Merge pateint dataset with above keywords to only get pateints that have status keywords.
#Read in pateint dataset
Data = pd.read_csv("DeltaData.txt",sep='\t' )
#Make keywords lowercase
Data['Status'] = Data['Status'].str.lower()
#Combine all keywords into df.
merge_list=dead_list+mild_list+moderate_list+very_severe_list+veryMild_asymptomatic_list
merge_list=pd.DataFrame({'Status': merge_list})

#Merge 
DeltaData=pd.merge(merge_list,Data,on=['Status'])
DeltaData.to_csv("DeltaData.tsv",sep='\t',mode='w',index=None)

