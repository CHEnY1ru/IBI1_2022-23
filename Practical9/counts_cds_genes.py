stop_condon=input('please input one of the stop codons(TAA, TAG, TGA):')
#the same method in Qeustion2. Write a function to make it clearer
def get_gene(stopcondon,outputfile):
    import re
    gene=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
    output_file=open(outputfile,'w')
    str_gene=gene.read()
    a=re.split('\n>',str_gene)
    for i in a:
        if i.endswith(stopcondon):
            #count the target seq
            new_i=""
            for line in i:
                line = line.strip()
                new_i+=line
            n=len(re.findall(stopcondon,new_i))
            i=re.sub('cdna.+]',str(n),i)
            j='>'+i+'\n'
            output_file.write(j)
#match the stop concon from the file
if stop_condon=='TAA':
    get_gene('TAA',"TAA_stop_genes.fa")
elif stop_condon=='TAG':
    get_gene('TAG',"TAG_stop_genes.fa")
elif stop_condon=='TGA':
    get_gene('TGA',"TGA_stop_genes.fa")
else:
    print('please input the right form')
