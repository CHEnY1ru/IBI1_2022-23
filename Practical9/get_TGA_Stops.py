import re
gene=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
output_file=open('TGA_genes.fa','w')
str_gene=gene.read()
#split the str into many short parts
a=re.split('\n>',str_gene)
#use a for loop to find the right DNA strings
for i in a:
    #judge if the string has TGA as stop concdon
    if i.endswith("TGA"):
        #remove the information we don't need
        i=re.sub('cdna.+]','',i)
        #make sure the format is correct
        j='>'+i+'\n'
        #change the file
        output_file.write(j)
