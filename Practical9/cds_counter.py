import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
#input your DNA into this function and get the number of matched parts
def count(seqs):
    stop_codons=['TAA','TAG','TGA']
    times=0
    for i in stop_codons:
        #use every condons in stop_condon to match the seq
        times= times+len(re.findall("(?={0})".format(i),seqs) ) 
    print(times)
count(seq)
