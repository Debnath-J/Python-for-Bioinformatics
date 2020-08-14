#Basic Protein Information Program
#This program will help to get neccessary information from given protein sequence.
#such as, length of the protein, number of aliphatic, aromatic, acidic, basic, hydroxylic, ulphur containing, amidic - amino acids
#The program will stop if it finds any invalid amino acids inside the sequence.

protein=input("Enter Your protein sequemce :").upper()                                              #Ask the protein sequence from user.

stop=""                                                                                             #Assigning "stop" without value, so that it can be used to stop the program to move further if it finds an invalid a.a.

for i in range(len(protein)):                                                                       #program will search throughout the end of the protein sequence to find if it has any invalid a.a.
    if protein[i] not in 'ACDEFGHIKLMNPQRSTVWY':                                                    #if the seq. has any character outside the standard single letter a.a. 
        stop="1"                                                                                    #this for loop will give a value to "stop"
        print("It is not a valid amino acid sequence !")                                            #and shows the user that it is not a valid seq.
        print("Your Protein sequence has invalid amino acid %s at position %d ."%(protein[i],i+1))  #along with that invalid character and it's position in the seq.
        

if stop!="1":                                                                                       #If the seq. contains not even a single invalid character, the value of stop will remain blank ( "" ) and this if function start working. otherwise, it won't.
    print("It is a valid amino acid sequence!\n")                                                   #showing the user that it is a valid amino acid seq.
    print("Length of your protein sequence:", len(protein))                                         #Showing Length
    print("Number of different kinds of amino acids in your sequence -")                            #and the amount of different kinds of amino acids in the sequence. 
    print("Aliphatic:", protein.count("A")+protein.count("G")+protein.count("I")+protein.count("L")+protein.count("P")+protein.count("V"))
    print("Aromatic:", protein.count("F")+protein.count("W")+protein.count("Y"))
    print("Acidic:", protein.count("D")+protein.count("E"))
    print("Basic:", protein.count("R")+protein.count("H")+protein.count("K"))
    print("Hydroxylic:", protein.count("S")+protein.count("T"))
    print("Sulphur containing:", protein.count("C")+protein.count("M"))
    print("Amidic:", protein.count("N")+protein.count("Q"))


    
