import sys
from Bio import SeqIO

fasta_in = sys.argv[1]

for record in SeqIO.parse(fasta_in, 'fasta'):
    id_part = record.id
    desc_part = record.description
    seq = record.seq

    print('id:', id_part)
    print('desc:', desc_part)
    print('seq:', seq)
