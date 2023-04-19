#question3
#set a function name and parameter
def judge_dna(DNA_seq):
    #i will use regular expression
    import re
    #re.I can allow the target_seq ignore if the letter is caplized
    target_seq=re.compile(r"ATG.+TGA",re.I)
    #find the target sequence in DNA
    get_seq_pre=re.findall(target_seq,DNA_seq)
    #take out the string from get_seq
    get_seq=get_seq_pre[0]
    #calculate percentage
    percentage= len(get_seq) / len(DNA_seq)*100
    print(len(get_seq))
    #judgement
    if percentage>50:
        return print("protein-coding, and the percentage is:",percentage,"%")
    elif percentage<10:
        return print("non-coding,and the percentage is:",percentage,"%")
    else:
        return print("unclear,and the percentage is:",percentage,"%")
#test
judge_dna("ATGGGGGTGAAAAAAAAA")
judge_dna("aaaaatgagtgtaagccTGAtaaaaaaTTTTTTTTTTTTTTTTTTTTTTT")
judge_dna("AATGagTGAaaaaaaaaaaaaaaaaaaaaGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
