import os


#os.chdir(r"C:\Users\15154\Desktop")



#Wildtype Sars seq
wtNSeq = open("ORF10_NC_045512.2_29557-29671.txt", "r")
wtNSeq=wtNSeq.read().splitlines()[0]
#List of substitution mutations
subs = open("subs.txt", "r")
subs=subs.read().splitlines()


#Make fasta file of ORF10 seqs with mutations. wt ORF10 on top. 
fasta=open("Seqs.fasta", "w")
fasta.write(">ORF10_wt")
fasta.write('\n')
fasta.write(wtNSeq[1:len(wtNSeq)])
fasta.write('\n')
for sub in subs:
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
