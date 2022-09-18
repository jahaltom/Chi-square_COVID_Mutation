import os
import pandas as pd


os.chdir(r"C:\Users\15154\Desktop\Chi-square_COVID_Mutation-main")




#Wildtype Sars seq
wtNSeq = open("data/ORF10_NC_045512.2_29557-29671.txt", "r")
wtNSeq=wtNSeq.read().splitlines()[0]
#List of substitution mutations
subs=pd.read_csv("DeltaDataWithKeywords.tsv",sep="\t")["substitutions"].dropna().drop_duplicates().tolist()



#Make fasta file of ORF10 seqs with mutations. wt ORF10 on top. 
fasta=open("Seqs.fasta", "w")
fasta.write(">ORF10_wt")
fasta.write('\n')
fasta.write(wtNSeq[1:len(wtNSeq)])
fasta.write('\n')
for sub in subs:
        if "," in sub: #Multiple substitution mutations in at least 1 viral seq. 
            MutNSeq=wtNSeq[1:] #To add multiple mutations to
            #List mutations
            mult_mut=sub.split(',')
            for m in mult_mut: 
                wt=m[0]
                mut=m[len(m)-1]
                pos=int(m[1:len(m)-1])-29557 #29557 is ORF10 start position in sarsCov2 genome. 
                #Check that wt allele in sub is what it should be according to wtNSeq. Write new nt seq with mutation to fasta.
                if wtNSeq[pos] == wt:         
                    MutNSeq=MutNSeq[:pos] + mut + MutNSeq[pos+1:]
                    print(MutNSeq)
            fasta.write(">"+sub)
            fasta.write('\n')
            fasta.write(MutNSeq)
            fasta.write('\n')   

        else:                
            wt=sub[0]
            mut=sub[len(sub)-1]
            pos=int(sub[1:len(sub)-1])-29557 #29557 is ORF10 start position in sarsCov2 genome. 
            #Check that wt allele in sub is what it should be according to wtNSeq. Write new nt seq with mutation to fasta.
            if wtNSeq[pos] == wt:
                fasta.write(">"+sub)
                fasta.write('\n')
                fasta.write(wtNSeq[1:pos] + mut + wtNSeq[pos+1:])
                fasta.write('\n')
fasta.close()
