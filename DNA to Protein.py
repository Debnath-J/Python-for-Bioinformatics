#!/usr/bin/python

#Translation
#To get all the possible ORFs and their translated amino acid sequence at once from six reading frame of user given DNA seq.
#To make translated protein seq. from RNA seq., replace all the "T"s with "U"s. Like, "ATG" to "AUG".

def translate(dna,frame):                                                               #Defining the function so that it can be used for multiple times
    for i in range(frame,len(dna),3):
        codon1=dna[i:i+3]
        if codon1=='ATG':
            position1=i
            for j in range(position1,len(dna),3):
                codon2=dna[j:j+3]
                if codon2 in ['TAA','TAG','TGA']:
                    position2=j
                    length_orf=(position2-position1)+3
                    orf=dna[position1:position2+3]
                    print(position1+1, "\t", position2+1, "\t", length_orf, "\t", orf)  #Till this, everything is similar as described in "Finding ORF.py"

                    protein=''                                                          #At first place, the protein (which will be built by following code of this program) is defined here using '' , which indicates that for now it has no value.

                    codon_aa = {"AAA":"K", "AAC":"N", "AAG":"K", "AAT":"N",             #Dictionary of all the possible 64 codons and their single letter amino acid product, which will be used later to build a complete amino acid seq.
                                "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T", 
                                "AGA":"R", "AGC":"S", "AGG":"R", "AGT":"S",
                                "ATA":"I", "ATC":"I", "ATG":"M", "ATT":"I", 

                                "CAA":"Q", "CAC":"H", "CAG":"Q", "CAT":"H", 
                                "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
                                "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R", 
                                "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",

                                "GAA":"E", "GAC":"D", "GAG":"E", "GAT":"D", 
                                "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A", 
                                "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G", 
                                "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V", 

                                "TAA":".", "TAC":"Y", "TAG":".", "TAT":"T",             # As these three stop codons (TAA,TAG,TGA) do not make any amino acids, their value is given "."
                                "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S", 
                                "TGA":".", "TGC":"C", "TGG":"W", "TGT":"C", 
                                "TTA":"L", "TTC":"F", "TTG":"L", "TTT":"F"}
                    
                    for i in range(0, len(orf), 3):                                     #Likewise for the ORFs, here, the program will also search search for codons (three base at a time) within the length of produced ORF in earlier section.
                        codon = orf[i:i+3]                                              #each codon will made of three nucleotides from ORF seq.
                        protein += codon_aa[codon]                                      #As the program meets the codon, it will compare them with the codon_aa dictionary and start building a protein seq.

                    length_protein=len(protein)-1                                       #Original length of the protein sequence will have one less amino acid, since no amino acid will be made from stop codon.
                    print("\t\t\t >> (", length_protein, ")", protein)                  #It's time to show the result!
                    break                                                               #The function will terminate as there is no need to continue when we get the complete translated amino acid seq from ORF.

dna=input('Enter your DNA sequence:').upper()                                           #Rest of the part will be same as the description of "Finding ORF.py"

print("\n")
print("\t=========>>> For Leading strand ")
print("\n")
print("From \t To \t Length \t Sequence")
print("===================================================\n")

print("\t\t(1st reading frame)\n")
print(translate(dna,0))

print("\n\t\t(2nd reading frame)\n")
print(translate(dna,1))

print("\n\t\t(3rd Reading frame)\n")
print(translate(dna,2))

#================================================================== Lagging strand ==========================================================================

basecomplement={'A':'T','C':'G','G':'C','T':'A'}
letters=list(dna)
dna2=[basecomplement[base] for base in letters]
dna3="".join(dna2)
    
print("\n")
print("\t For Lagging strand <<<=========")
print("\n")

print("From \t To \t Length \t Sequence")
print("===================================================\n")
   
print("\t\t(1st reading frame)\n")
print(translate(dna3,0))

print("\n\t\t(2nd reading frame)\n")
print(translate(dna3,1))

print("\n\t\t(3rd Reading frame)\n")
print(translate(dna3,2)
