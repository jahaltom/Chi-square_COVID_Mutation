# Chi-square_COVID_Mutation
Chi-square test on COVID-19 mutations and clinical severity.

Conditions are: Very-Mild_Asymptomatic, Mild, Moderate, Very_Severe, and Dead.



**DataProcessing.py**
This script takes in the patient dataset as a tab delimited txt file like from excel (AlphaData.txt, DeltaData.txt, OmicronData.txt), and generates a tsv file that only contains patients with keywords.


**ORF10_Chi-Square_Test.py**
Once DataProcessing.py is run, this script performs the Chi-Square Test in two modes.

Performs Chi-Square Test for 1 specific condition vs all others.
```
ChiSqr_All(Strain,mut,muts[mut],Strains[Strain],"Dead")
```

#Performs Chi-Square Test for two specific conditions. The less severe condition must always go on the left like below. 
```
ChiSqr_Two(Strain,mut,muts[mut],Strains[Strain],"Mild","Dead")
```

Outputs results in tsv file
![alt text](https://github.com/jahaltom/Chi-square_COVID_Mutation/blob/main/ChiSquareOutput.jpg?raw=true)






# Predict SNP effect

**ntMuts2AAMuts.py:** Uses wild-type SarsCov2 ORF10 (NC_045512.2) nt seq and list of substitution mutations from E.g. DeltaDataWithKeywords.tsv (A29567G) to generate fasta files(nt an AA) containing seqs with given mutations. Also outputs list of AA mutations.

**PredictSNP**
PredictSNP is a consensus
classifier combining six best performing prediction methods to provide more accurate and robust
alternative to the predictions delivered by individual integrated tools


PredictSNP (https://loschmidt.chemi.muni.cz/predictsnp1/) cannot have mutations in which there is a * (R24*), so the previous script generates a specific list for PredictSNP in which the * mutations are removed. 
Only looks at as single mutations for each call. 
![alt text](https://github.com/jahaltom/Chi-square_COVID_Mutation/blob/main/PredictSNP.PNG?raw=true)

**DataCuration.py** Curates all of the above data into a tsv. 

**Other Analysis**
The defualt is for the Delta variant dataset, to do other variants see runall.sh
