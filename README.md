# Chi-square_COVID_Mutation
Chi-square test on COVID-19 mutations and clinical severity (Very-Mild_Asymptomatic,Mild,Moderate,Very_Severe,Dead).



**DataProcessing.py**
Takes in keywords txt files and makes all characters lowercase and then updates the input txt file. This way one can add addidtional keywords to a group. 
Additionaly, this script takes in the patient dataset as a tab delimited txt (like from excel. AlphaData.txt,DeltaData.txt), and generates a tsv file that only contains patients with keywords.


**ORF10_Chi-Square_Test_2.py**
Once DataProcessing.py is run, this script performs the Chi-Square Test in two modes.

Performs Chi-Square Test for 1 specific group vs all others.
```
ChiSqr_All(Strain,mut,muts[mut],Strains[Strain],"Dead",results)
```

#Performs Chi-Square Test for two specific groups
```
ChiSqr_Two(Strain,mut,muts[mut],Strains[Strain],"Very_Severe","Very-Mild_Asymptomatic",results)
```

Outputs results in tsv file
```
Strain	Mutation	Has Mutation	Very-Mild_Asymptomatic	Mild	Moderate	Very_Severe	Dead	Mild vs Dead
AY.34 (509)	A29618G (1)	Mut+	0	1	0	0	0	4.30312E-13
AY.34 (509)	A29618G (1)	Mut-	0	422	82	2	2	4.30312E-13
```
