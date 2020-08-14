#!/usr/bin/python

#ORF

#Defining orf(dna,frame) so that it can be used for multiple times to get all the possible orfs for different frames and DNA strands.

def orf(dna,frame):                                         #defining
    for i in range(frame,len(dna),3):                       #it will start to search three base at a time from the frame(0/1/2) of DNA to the length of DNA
        codon1=dna[i:i+3]                                   #codon1 will contain three nucleotide
        if codon1=='ATG':                                   #when codon meets the start codon(ATG) in DNA seq., it will trigger this if function
            position1=i                                     #by marking the position1 with i, it gets a value and program will remember it's position for later work.
            #Now it's time for searching the stop codon to complete the orf.
            for j in range(position1,len(dna),3):           #Now the program will start to search for stop codon starting from position 1 (start codon) to the end of DNA sequence.           
                codon2=dna[j:j+3]                           #like codon1, codon2 will also contain three nucleotide
                if codon2 in ['TAA','TAG','TGA']:           #While searching, if codon2 meets any of the three stop codons it will trigger the following code.
                    position2=j                             #To store the value of the position of stop codon, position2 is marked with a value "j"
                    length=(position2-position1)+3          #So the length of the orf will be: (from position2 to position1) plus 3, to compensate the loss of stop_codon( 3 nucleotide ).
                    orf=dna[position1:position2+3]          #For building the orf, now we need to just show the python from which position to which position it needs to consider (here, position1 as start and position2 for stop)
                    print(position1+1, "\t", position2+1, "\t", length, "\t", orf)  #As the ORF is built, it is time to display it to the user with the start, end and it's length.
                    break                                   #As the program gets the stop codon, we don't need to move forward. Since, an ORF finishes in the stop codon.

dna=input('Enter your DNA sequence:').upper()               #Ask the user to enter DNA sequence.

print("\n")
print("\t=========>>> For Leading strand ")                 #As the first part will display only the ORFs from the leading strand (5'-3').
print("\n")
print("From \t To \t Length \t Sequence")                   #As I am going to making a table, they (From/To/Length/Sequence) will be my header.
print("===================================================\n")

print("\t\t(1st reading frame)\n")
print(orf(dna,0))                                           #dna,0-indicates the python to look for ORFs from 1st reading frame of the DNA seq.

print("\n\t\t(2nd reading frame)\n")
print(orf(dna,1))                                           #dna,1-for the 2nd

print("\n\t\t(3rd Reading frame)\n")
print(orf(dna,2))                                           #dna,2-for the 3rd

#=========================== For Riverese strand ==========================================

print("\n")
print("\t For Lagging strand <<<=========")                 #Now this program gonna make a reverse complement of the given DNA seq. (3'-5') and will show all the ORFs form there.
print("\n")

basecomplement={'A':'T','C':'G','G':'C','T':'A'}            #Likewise the previous Basic_DNA.py, this program will reverse the DNA seq. using the same code.
letters=list(dna)
dna2=[basecomplement[base] for base in letters]
dna3="".join(dna2)                                          # "dna3" will be the reverse complementary strand (3'-5') of the given DNA seq.

print("From \t To \t Length \t Sequence")                   
print("===================================================\n")

print("\t\t(1st reading frame)\n")
print(orf(dna3,0))

print("\n\t\t(2nd reading frame)\n")
print(orf(dna3,1))

print("\n\t\t(3rd Reading frame)\n")
print(orf(dna3,2))

input("Press Enter key to exit _")                          #When the user press Enter key, this program will be closed.
