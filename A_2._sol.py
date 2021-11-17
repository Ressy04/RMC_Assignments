# Q1. Program to find the second maximum GC value from the list also find the median GC value.
#     Gc values are as follows 30.5,12,54,23,84

gc_values=[30.5,12,54,23,84]
print("GC values: ",gc_values)
gc_values.sort()
print("Sorted GC values: ",gc_values)
print("Second maximum GC value: ",gc_values[-2])
median=int(len(gc_values)/2)
print("Median of the GC values: ",gc_values[median])

# Q2. Program to check which stop codons are present in the sequence UAAAAGGCGAGAUAAAUA.

seq="UAAAAGGCGAGAUAAAUA"
print("Sequence: ",seq)
stop_codons="UAA","UAG","UGA"
print("UAA present: ","UAA"in seq)
print("UAG present: ","UAG"in seq)
print("UGA present: ","UGA"in seq) 

# Q3. Check the presence of all the stop codons in the list ["UAA","UGC","AUAGCT","ATUA","UAG"] 

seq= ["UAA","UGC","AUAGCT","ATUA","UAG"]
print(seq)
print("UAA: ",seq.count("UAA")) 
print("UAG: ",seq.count("UAG")) 
print("UGA: ",seq.count("UGA"))

# Q4. Program to transcribe the sequence "ATGCTCGCGTAA"

seq="ATGCTCGCGTAA"
print("Sequence before transcription: ",seq)
transcription=seq.replace("T","U")
transcription=seq.replace("T","U")
print("Sequence after Transcription: ",transcription)


#Q5. Concatenate two lists of GC Values [30.5,12,54,23,84] and [12,45,54,32] 
#     and find the maxium and minum GC Values.

gc_1=[30.5,12,54,23,84]
gc_2=[12,45,54,32]
concat=(gc_1+gc_2)
print("Concatenated GC values: ",concat)
print("Maximum GC value: ",max(concat))
print("Minimum GC value: ",min(concat))