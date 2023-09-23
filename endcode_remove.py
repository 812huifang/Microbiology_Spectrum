from sys import argv
from Bio import SeqIO
from Bio.Seq import Seq

script, input, input1, output, output1 = argv
output_file = open(output, "w")
output_file1 = open(output1, "w")
input_file = SeqIO.parse(input, "fasta")
input_file1 = SeqIO.parse(input1, "fasta")
list = []
for sequence in input_file:
 	if "*" in str(sequence.seq):
 		list.append(str(sequence.id))
 	else:
 		SeqIO.write(sequence, output_file, "fasta")
for seq in input_file1:
	if str(seq.id) in list:
		pass
	else:
		SeqIO.write(seq, output_file1, "fasta")
