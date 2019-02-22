from Bio import SeqIO
import sys

def getGC(seq):
	return(str(int(round((sum([1.0 for nucl in seq if nucl in ['G', 'C']]) / len(seq)) * 100))))

def processFasta(fas):
	print("identifier\tGCcontent\tlength")
	for record in SeqIO.parse(fas, "fasta"):
		print("{}\t{}\t{}".format(record.id, getGC(str(record.seq)), str(len(record.seq))))
    
processFasta(sys.argv[1])
