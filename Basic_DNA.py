#Basic_DNA
"""This program is designed to get basic information from DNA like
length of a DNA sequence, number of A/T/C/G, number of purine and pyrimidine bases,
gc content,unidentified bases, reverse complementary sequences."""

dna=input("Enter your DNA seqeuence here:").lower() #take DNA seq. from user

print("Length of your given DNA seqeucne is", len(dna)) #to get the length
print("Your DNA sequence contains:", dna.count('a'),"Adenine; ", dna.count('c'),"Cytosine; ",dna.count('g'),"Guanine; ",dna.count('t'),"Thymine.") #to get the number of bases
print("Purine:", dna.count('a')+dna.count('g')) #number of purine bases
print("Pyrimidine:", dna.count('c')+dna.count('t')) #number of pyrimidine bases
print("GC content:", (dna.count('c')+dna.count('g'))*100/len(dna)) #gc content
print("Unidentified bases:", dna.count('n')) #unidentified bases (n)

#Reverse Complementary Sequences

dna2=dna[::-1] #to reverse the dna
basecomplement={'a':'t','c':'g','g':'c','t':'a'} #complementary bases for bases in leading strand
letters=list(dna2) #make a list from the DNA string
dna2=[basecomplement[base] for base in letters] #To substitue the bases of DNA with complementary bases.
dna2=''.join(dna2) #make it a string again.
print("Reverse transcription of your given DNA seqeuence:")
print(dna2) #to show the result
