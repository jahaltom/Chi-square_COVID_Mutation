# Chi-square_COVID_Mutation
Chi-square test on COVID-19 mutations and clinical severity.

Conditions are: Very-Mild_Asymptomatic, Mild, Moderate, Very_Severe, and Dead.



**DataProcessing.py**
This script takes in the patient dataset as a tab delimited txt file like from excel (AlphaData.txt, DeltaData.txt, OmicronData.txt), and generates a tsv file that only contains patients with keywords.


**ORF10_Chi-Square_Test_2.py**
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
![alt text](https://github.com/jahaltom/Chi-square_COVID_Mutation/blob/main/OutputExample.PNG?raw=true)




**Other Analysis**
The above was for the Delta variant dataset (DeltaData.txt). To use another variant data set (E.g. AlphaData.txt), simply swap the word Delta with Alpha.
```
sed -i 's/Delta/Alpha/g' DataProcessing.py
sed -i 's/Delta/Alpha/g' ORF10_Chi-Square_Test.py
```
Then re-run DataProcessing.py and ORF10_Chi-Square_Test.py.
