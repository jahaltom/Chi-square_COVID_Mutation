import pandas as pd
from scipy.stats import chi2_contingency

results=[]


#Given a dataframe of patients, returns total # patients and total # patients belonging to each condition. Returns list of ints.
def catagorize(df):
    #Total # patients
    Total=len(df.index)
    dead=0
    for i in dead_list:
        dead=dead+len(df[df['Status'] == i])
    mild=0
    for i in mild_list:
        mild=mild+len(df[df['Status'] == i])
    very_severe=0
    for i in very_severe_list:
        very_severe=very_severe+len(df[df['Status'] == i])
    moderate=0
    for i in moderate_list:
        moderate=moderate+len(df[df['Status'] == i])
    veryMild_asymptomatic=0
    for i in veryMild_asymptomatic_list:
        veryMild_asymptomatic=veryMild_asymptomatic+len(df[df['Status'] == i])
    return (Total,veryMild_asymptomatic,mild,moderate,very_severe,dead)



def Condition(CondState):
        #Get index number of condition(s)
        if CondState == "Very-Mild_Asymptomatic":
            return 1
        if CondState == "Mild":
            return 2
        if CondState == "Moderate":
            return 3
        if CondState == "Very_Severe":
            return 4
        if CondState == "Dead":
            return 5
   


#Takes in a dataframe for the whole Strain(df_Strain), and a df for a particular mutation in that Strain (df_mut). Strain and mut are strings that contain Strain name and mutation(E.g. A29558T).
#CondState and OtherCondState is the condition of the patient(Mild, Very_Severe, Moderate, Very-Mild_Asymptomatic, Dead).

#Performs Chi-Square Test for two specific conditions. The less severe condition must always go on the left.
def ChiSqr_Two(Strain,mut,df_mut,df_Strain,CondState,OtherCondState):
        global results    
        mut_list=catagorize(df_mut)
        Strain_list=catagorize(df_Strain)     
        #Get index number of conditions
        CondNum=Condition(CondState) 
        OtherCondNum=Condition(OtherCondState)
        #Total with strain and total with mutation
        mut_total=mut_list[0]  
        Strain_total=Strain_list[0]
        #Total with condition in strain and with mutation   
        mut_Cond=mut_list[CondNum]
        strain_Cond=Strain_list[CondNum]       
        #Other Condition
        mut_OtherCond=mut_list[OtherCondNum]
        strain_OtherCond=Strain_list[OtherCondNum]     
        #construct contingency table
        isCond=["Cond"]*mut_Cond
        isMut=["Yes"]*mut_Cond
        isCond=isCond+["other_Cond"]*(mut_OtherCond)
        isMut=isMut+["Yes"]*(mut_OtherCond)
        isCond=isCond+["Cond"]*(strain_Cond-mut_Cond)
        isMut=isMut+["no"]*(strain_Cond-mut_Cond)
        isCond=isCond+["other_Cond"]*(strain_OtherCond-mut_OtherCond)
        isMut=isMut+["no"]*(strain_OtherCond-mut_OtherCond)
        df = pd.DataFrame({'isCond' : isCond ,'isMut' : isMut })
        contigency= pd.crosstab(df['isCond'], df['isMut'])  
        
        try:
            mutRatio=((contigency["Yes"][0]/(Strain_total))/(contigency["Yes"][1]/(Strain_total)))
            wuhanRatio=((contigency["no"][0]/(Strain_total))/(contigency["no"][1]/(Strain_total)))
        except:
            mutRatio="NA"
            wuhanRatio="NA"
        #There must be at least 1 person with the mutation in ether condition. 
        if mut_Cond !=0 or mut_OtherCond !=0: 
  
                # Chi-square test of independence.
                c, p, dof, expected = chi2_contingency(contigency)             
                #Write results
                #Get the number of patients without mutation for each condition. 
                nonMut_list=[x - y for x, y in zip(Strain_list, mut_list)]    
                #does mutation increase severity? 
               
                #Get stats
                mut_list=[Strain,str(Strain_total-mut_total),mut,str(mut_total),str(mut_total),"Mut+"]+list(mut_list)+[p]+ [mutRatio ]    
                nonMut_list=[Strain,str(Strain_total-mut_total),mut,str(mut_total),str(Strain_total-mut_total),"Mut-"]+list(nonMut_list)+[p]+[wuhanRatio]
                results_temp=pd.DataFrame([mut_list,nonMut_list],columns=['Strain','Wuhan Strain Total','Mutation','Mutation Total','Table Total','Has Mutation','Total','Very-Mild_Asymptomatic', 'Mild', 'Moderate', 'Very_Severe', 'Dead',CondState+" vs "+OtherCondState + " P-value","("+CondState+"/Total) / ("+OtherCondState+"/Total)"]) 
                results_temp=results_temp.drop(['Total'], axis=1)
                results.append(results_temp)




#Performs Chi-Square Test for 1 specific condition vs all others.
def ChiSqr_All(Strain,mut,df_mut,df_Strain,CondState):
        global results
        mut_list=catagorize(df_mut)
        Strain_list=catagorize(df_Strain)

        #Get index number of condition(s)
        CondNum=Condition(CondState)


        mut_total=mut_list[0]
     

        Strain_total=Strain_list[0]
        mut_Cond=mut_list[CondNum]
        strain_Cond=Strain_list[CondNum]



        #construct contingency table
        isCond=["Cond"]*mut_Cond
        isMut=["Yes"]*mut_Cond

        isCond=isCond+["not_Cond"]*(mut_total-mut_Cond)
        isMut=isMut+["Yes"]*(mut_total-mut_Cond)

        isCond=isCond+["Cond"]*(strain_Cond-mut_Cond)
        isMut=isMut+["no"]*(strain_Cond-mut_Cond)

        isCond=isCond+["not_Cond"]*((Strain_total-mut_total)-(strain_Cond-mut_Cond))
        isMut=isMut+["no"]*((Strain_total-mut_total)-(strain_Cond-mut_Cond))

        contigency = pd.DataFrame({'isCond' : isCond ,'isMut' : isMut })
        contigency= pd.crosstab(contigency['isCond'], contigency['isMut'])

        try:
            mutRatio=((contigency["Yes"][0]/(Strain_total))/(contigency["Yes"][1]/(Strain_total)))
            wuhanRatio=((contigency["no"][0]/(Strain_total))/(contigency["no"][1]/(Strain_total)))
        except:
            mutRatio="NA"
            wuhanRatio="NA"
        
        # Chi-square test of independence.
        c, p, dof, expected = chi2_contingency(contigency)

        #Write results
 
        #Get the number of patients without mutation for each condition. 
        nonMut_list=[x - y for x, y in zip(Strain_list, mut_list)]
        #Get stats
        mut_list=[Strain,str(Strain_total-mut_total),mut,str(mut_total),str(mut_total),"Mut+"]+list(mut_list)+[p] + [mutRatio]       
        nonMut_list=[Strain,str(Strain_total-mut_total),mut,str(mut_total),str(Strain_total-mut_total),"Mut-"]+list(nonMut_list)+[p] + [wuhanRatio]
        results_temp=pd.DataFrame([mut_list,nonMut_list],columns=['Strain','Wuhan Strain Total','Mutation','Mutation Total','Table Total','Has Mutation','Total','Very-Mild_Asymptomatic', 'Mild', 'Moderate', 'Very_Severe', 'Dead',CondState+" vs All others P-Value","("+CondState+"/Total) / (All Others/Total)"])
        results_temp=results_temp.drop(['Total'], axis=1)
        results.append(results_temp)



#Keywords that place a patient in a category
with open ("keywords/Dead.txt") as f:
        dead_list=f.read().splitlines()
with open ("keywords/Mild.txt") as f:
        mild_list=f.read().splitlines()
with open ("keywords/Moderate.txt") as f:
        moderate_list=f.read().splitlines()
with open ("keywords/Very_Severe.txt") as f:
        very_severe_list=f.read().splitlines()
with open ("keywords/VeryMild_Asymptomatic.txt") as f:
        veryMild_asymptomatic_list=f.read().splitlines()

#Read in COVID data
Data = pd.read_csv("DeltaDataWithKeywords.tsv",sep='\t',encoding = 'unicode_escape')
#Create dict of dfs with each Strain as a key. The dfs will contain patients that go with the Strain.
Strains = dict(tuple(Data.groupby('Strain')))

for Strain in Strains.keys():
   #Create dict of dfs with each mutation as a key. The dfs will contain patients that go with the mutation.
   muts=dict(tuple(Strains[Strain].groupby('Mutations')))
   for mut in muts.keys():
       #The less sever condition must always go on the left for ChiSqr_Two.
       
       #Get wildtype only from strain an concat mut onto.
       s=Strains[Strain][Strains[Strain]["Mutations"].isnull()]
       df=pd.concat([s,muts[mut]]) 
       # ChiSqr_Two(Strain,mut,muts[mut],Strains[Strain],"Very-Mild_Asymptomatic","Dead")           
       # ChiSqr_Two(Strain,mut,muts[mut],Strains[Strain],"Mild","Moderate")
       # ChiSqr_Two(Strain,mut,muts[mut],Strains[Strain],"Mild","Dead")
       # ChiSqr_Two(Strain,mut,muts[mut],Strains[Strain],"Moderate","Dead")     
       # ChiSqr_Two(Strain,mut,muts[mut],Strains[Strain],"Very_Severe","Very-Mild_Asymptomatic")
       # ChiSqr_Two(Strain,mut,muts[mut],Strains[Strain],"Very_Severe","Mild")
       ChiSqr_Two(Strain,mut,muts[mut],df,"Mild","Moderate")
       ChiSqr_All(Strain,mut,muts[mut],df,"Mild")
       
#Concat list of dfs
results = pd.concat(results)
#Get column order
col_order= results.columns.to_list()
#Collapse data 
results=results.groupby(['Strain','Mutation','Has Mutation'],as_index=False).first()
#Set to original column order
results=results[col_order]

results.to_csv("DeltaResults.tsv",sep='\t',mode='w',index=None)
