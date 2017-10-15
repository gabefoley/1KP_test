from Bio import SeqIO

records = SeqIO.parse("files/CYP711_uncleaned.fasta", "fasta")

for record in records:
    print (record)
    print (record.name)
    print (record.description)