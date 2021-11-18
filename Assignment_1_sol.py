# Q1 Calculate the length of DNA Sequence

seq=input("Enter a DNA sequence: ")
length=len(seq)
print("Length of the entered sequence is: ",length)

# Q2 Calculate the GC percentage of DNA sequence

seq=input("Enter a DNA sequence: ")
gc_percentage=100*(seq.count("G")+seq.count("C"))/len(seq)
print("GC% of the entered sequence is: ",gc_percentage)
 
# Q3 Mutate a sequence taken from user. Take position and mutated base as argument

#substitution
seq=input("Enter a sequence: ")
substitution=seq.replace("A","G")
print("Sequence after Substitution: ",substitution)

#inversion
seq=input("Enter a sequence of length > 5 nucleotide bases: ")
print("Sequence before inversion: ",seq )
random_seq_break=seq[4:]                         # random chromosome break
rest_of_seq=seq[:4]
rev_random_break=random_seq_break[::-1]          # reversal
inversion=(rest_of_seq+rev_random_break)         # re-insertion
print("Sequence after inversion : ",inversion)

# Q4 Slice the sequence in two halves

seq=input("Enter a sequence: ")
l=len(seq)
first_half=seq[:int(l/2)]
second_half=seq[int(l/2):]
print(first_half,second_half)

# Q5 Position of the 2nd occurrence of “A”  in the sequence “ATCGATAGATACAA”

seq="ATCGATAGATACAA"
print("Number of A's in the seq: ",seq.count("A"))
print("Index of first A: ",seq.find("A"))
sec_oc=seq.find(("A"),seq.find("A")+1)
print("Index of second A: ",sec_oc)

# Q6 Program to check which stop codons are present in the sequence  “UAAAAGGCGAGAUAAAUA”

seq="UAAAAGGCGAGAUAAAUA"
stop_codons="UAG","UAA","UGA"
print("Sequence: ",seq)
print("UAG is present : ","UAG" in seq)
print("UAA is present : ","UAA" in seq)
print("UGA is present : ","UGA" in seq)

# Q7 Frequencies of the restriction enzyme recognition sites ["ACGTC","CTAGT","ATGCTA"] in 
# the DNA sequences of delta strain of COVID 19.

## (File info: >OK091006.1 Severe acute respiratory syndrome coronavirus 2 isolate
##  SARS-CoV-2/human/JPN/SARS-CoV-2,B.1.617.2 lineage, Delta variant/2021, complete genome)

file=open(r"C:\Users\Arulkani\Desktop\Github\RMC_Assignments\delta_strain_cov19.fasta")
seq=file.read()
res_enz_recog_sites=["ACGTC","CTAGT","ATGCTA"]
print("Frequency of ACGTC in the delta stain: ",seq.count("ACGTC"))
print("Frequency of CTAGT in the delta stain: ",seq.count("CTAGT"))
print("Frequency of ATGCTA in the delta stain: ",seq.count("ATGCTA"))
file.close()

# Q8 Program to reverse the second half region of a DNA sequence "ATGATAGATAGATGATATCGATAGTA"

seq="ATGATAGATAGATGATATCGATAGTA"
l=len(seq)
first_half=seq[:int(l/2)]
second_half=seq[int(l/2):]
reversed_seq=second_half[::-1] 
print("Given DNA sequence: ",seq)
print("Reversed 2nd half : ",first_half+reversed_seq)
