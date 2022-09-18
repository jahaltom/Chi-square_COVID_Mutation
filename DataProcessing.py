import os
import pandas as pd




#Make all keywords lowercase in tsv files and remake files as tsv. 
with open ("keywords/Dead.txt") as f:
        dead_list=f.read().splitlines()
        temp=[x.lower() for x in dead_list]
        dead_list=temp
        dead_df=pd.DataFrame(dead_list).drop_duplicates()
        dead_df.to_csv("keywords/Dead.txt",sep='\t',mode='w',index=None,header=None)
        
with open ("keywords/Mild.txt") as f:
        mild_list=f.read().splitlines()
        temp=[x.lower() for x in mild_list]
        mild_list=temp
        mild_df=pd.DataFrame(mild_list).drop_duplicates()
        mild_df.to_csv("keywords/Mild.txt",sep='\t',mode='w',index=None,header=None)
          
        
with open ("keywords/Moderate.txt") as f:
        moderate_list=f.read().splitlines()
        temp=[x.lower() for x in moderate_list]
        moderate_list=temp
        moderate_df=pd.DataFrame(moderate_list).drop_duplicates()
        moderate_df.to_csv("keywords/Moderate.txt",sep='\t',mode='w',index=None,header=None)
    
with open ("keywords/Very_Severe.txt") as f:
        very_severe_list=f.read().splitlines()
        temp=[x.lower() for x in very_severe_list]
        very_severe_list=temp
        very_severe_df=pd.DataFrame(very_severe_list).drop_duplicates()
        very_severe_df.to_csv("keywords/Very_Severe.txt",sep='\t',mode='w',index=None,header=None)

        
with open ("keywords/VeryMild_Asymptomatic.txt") as f:
        veryMild_asymptomatic_list=f.read().splitlines()
        temp=[x.lower() for x in veryMild_asymptomatic_list]
        veryMild_asymptomatic_list=temp
        veryMild_asymptomatic_df=pd.DataFrame(veryMild_asymptomatic_list).drop_duplicates()
        veryMild_asymptomatic_df.to_csv("keywords/VeryMild_Asymptomatic.txt",sep='\t',mode='w',index=None,header=None)

 
#Read in pateint dataset       
#Some pateints will be excluded becuase they failed to have a status keyword. Merge pateint dataset with above keywords to only get pateints that have status keywords.
Data = pd.read_csv("data/DeltaData.txt",sep='\t',encoding = 'unicode_escape' )
#Make keywords lowercase
Data['Status'] = Data['Status'].str.lower()
#Combine all keywords into df.
merge_list=dead_list+mild_list+moderate_list+very_severe_list+veryMild_asymptomatic_list
merge_list=pd.DataFrame({'Status': merge_list})

#Merge  
data_withkeywords=pd.merge(merge_list,Data,on=['Status'])
data_withkeywords.to_csv("DeltaDataWithKeywords.tsv",sep='\t',mode='w',index=None)
