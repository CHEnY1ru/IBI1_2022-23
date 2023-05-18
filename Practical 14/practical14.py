'''Attention: this program runs slowly, maybe it will take 2 minutes to output a file. 
So please don't regard it as a broken program after you run it for a long time...... Sorry for my noob coding skill'''
#use pandas to create excel file
import pandas as pd
#can read xml file
import xml.dom.minidom
DOMTree=xml.dom.minidom.parse("go_obo.xml")
#get a collection of elements 
collection=DOMTree.documentElement
#get all the elements called "term"
terms=collection.getElementsByTagName("term")
#three lists to store ID,name,and defstr
ID=[]
Name=[]
defstr=[]
#search for the targeted terms and get the information of ID,name,defstr
for term in terms:
    defstr_str=term.getElementsByTagName("defstr")[0].childNodes[0].data
    if "autophagosome" in defstr_str:
        id=term.getElementsByTagName("id")[0].childNodes[0].data
        name=term.getElementsByTagName("name")[0].childNodes[0].data
        ID.append(id)
        Name.append(name)
        defstr.append(defstr_str)
#set a function to calculate childnodes
def Node(id):
    num=0
    for term in terms:
        term_id=term.getElementsByTagName("id")[0].childNodes[0].data
        term_is_a=term.getElementsByTagName("is_a")
        for i in term_is_a:
            term_isa=i.childNodes[0].data
            if term_isa==id:
                num+=1
                #This code uses the concept of recursion to call the main function multiple times until the last one has been traversed.
                num+=Node(term_id)
    return num
childnode=[]
for i in ID:
    childnode.append(Node(i))
data = {'ID': ID, 'Name': Name, 'defstr': defstr, 'childnode': childnode}
df = pd.DataFrame(data)
df.to_excel('autophagosome.xlsx', index=False)
