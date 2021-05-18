from Bio import Entrez

Entrez.email = "joy.debnath.ge@gmail.com"

Org = input("Enter Organism name: ")
ge = input("Enter Gene name: ")

full = Org + "[Orgn] " + "AND " + ge + "[Gene]"

handle = Entrez.esearch(db ="nucleotide", term=full, idtype="acc")

record = Entrez.read(handle)
rlist = record["IdList"]
frlist = rlist[0]
rcount = record["Count"]
print("\n", rcount, " Results found!")
print("\nfirst top 20 results:\n", rlist)
print("\n\nShowing result for :", frlist, "\n")

handle2 = Entrez.efetch(db="nucleotide", id=frlist, rettype="gb", retmode="text")
print(handle2.read())
