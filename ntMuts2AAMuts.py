from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import pandas as pd




########################  Write nucleotide fasta
#Wildtype Sars seq
wtNSeq = open("data/ORF10_NC_045512.2_29557-29671.txt", "r")
wtNSeq=wtNSeq.read().splitlines()[0]
#List of substitution mutations
subs=pd.read_csv("DeltaDataWithKeywords.tsv",sep="\t")["substitutions"].dropna().drop_duplicates().tolist()



#Make fasta file of ORF10 seqs with mutations. wt ORF10 on top.
fasta=open("ntSeqs.Delta.fasta", "w")
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



##################  Write AA fasta 
with open("AAseq.Delta.fasta", 'w') as aa_fa:
    for dna_record in SeqIO.parse("ntSeqs.Delta.fasta", 'fasta'):
        aa=dna_record.seq.translate()
        aa_record = SeqRecord(aa, id=dna_record.id,description="")
        SeqIO.write(aa_record, aa_fa, 'fasta')
        
        
        
        
        

######## Generate txt file with AA mutations and ID(T29589C). Generate file without ID as well for PREDICTSNP
AAMut=open("AAMut.Delta.txt", "w")
align = open("AAseq.Delta.fasta", "r")
mutList=[] #To be used with PREDICTSNP
for seq in align:
    ID=seq.strip()
    if ID == ">ORF10_wt":
        wtPSeq=next(align, '').strip()
    else:
        mut_seq=next(align, '').strip() 
        if len(mut_seq)==len(wtPSeq):
            for AA in range(0, len(mut_seq)):
                if mut_seq[AA] != wtPSeq[AA]:                   
                    AAMut.write(str(ID+" "+wtPSeq[AA]+str(AA+1)+mut_seq[AA]))
                    AAMut.write('\n')
                    mutList.append(wtPSeq[AA]+str(AA+1)+mut_seq[AA])
   

# Generate file for PREDICTSNP
df=pd.DataFrame(mutList).drop_duplicates()
df=df[~df.stack().str.contains('\*').any(level=0)]
df.to_csv("DeltaMut_PREDICTSNP.txt",sep='\t',index=False,mode='w',header=None)    

