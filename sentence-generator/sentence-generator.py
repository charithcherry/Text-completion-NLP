# sentence-generator to generate simple sentences
# By Hannah Newman <HN860433@wcupa.edu>

import random
from csv import DictWriter

# nouns & adjectives from https://github.com/janester/mad_libs
# determiners and prepositions from handouts from my linguistics class
# verbs from my brain

# get adjectives
with open("adj.txt","r") as adj_file:
    adjectives = adj_file.read().split("\n")

# get nouns
with open("nou.txt","r") as noun_file:
    nouns = noun_file.read().split("\n")

# get transitive verbs
with open("verbtr.txt", "r") as vtr_file:
    verbs_tr = vtr_file.read().split("\n")

# get intransitive verbs
with open("verbitr.txt", "r") as vitr_file:
    verbs_itr = vitr_file.read().split("\n")

# get determiners
with open("det.txt", "r") as det_file:
    determiners = det_file.read().split("\n")

# get prepositions
with open("pre.txt", "r") as prep_file:
    prepositions = prep_file.read().split("\n")

with open("pro.txt", "r") as pro_file:
    pronoun = pro_file.read().split("\n")    




with open("pverb.txt", "r") as pverb_file:
    pverb = pverb_file.read().split("\n")

with open("pnoun.txt", "r") as pnoun_file:
    pnoun = pnoun_file.read().split("\n")

with open("padverb.txt", "r") as padverb_file:
    padverb = padverb_file.read().split("\n")

# make a sentence!
def S():
    # every sentence has a noun phrase and a verb phrase
    res = NP() + " " + VP()
    # ~80% of the time, a prepositional phrase is added
    if random.random() < 0.8:
        # ~50% of prepositional phrases come after the NP+VP
        if random.random() < 0.5:
            res = res + " " + PP()
        else:
            res = PP() + ", " + res
    # capitalizes sentence and adds period
    return res.capitalize() + "."

# make noun phrase
def NP():
    res = ""
    # determiner ~99% of the time
    if random.random() < 0.99:
        res += det() + " "
    # adjective ~30% of the time
    if random.random() < 0.3:
        res += adj() + " "
    # noun 100% of the time
    res += n()
    # prepositional phrase ~3% of the time
    if random.random() < 0.03:
        res += " " +PP()
    return res

# make verb phrase
def VP():
    # ~50% of verb phrases are transitive & have a noun phrase
    if random.random() < 0.5:
        return v_tr() + " " + NP()
    # the other ~50% are just an intransitive verb
    else:
        return v_itr()

# make prepositional phrase
def PP():
    # a prepositional phrase is a preposition and a noun phrase
    return prep() + " " + NP()

# functions to get individual words
def v_itr():
    return verbs_itr[random.randint(0,len(verbs_itr)-1)]
def v_tr():
    return verbs_tr[random.randint(0,len(verbs_tr)-1)]
def n():
    return nouns[random.randint(0,len(nouns)-1)]
def adj():
    return adjectives[random.randint(0,len(adjectives)-1)]
def det():
    return determiners[random.randint(0,len(determiners)-1)]
def prep():
    return prepositions[random.randint(0,len(prepositions)-1)]
def pro():
    return pronoun[random.randint(0,len(pronoun)-1)]



def adverb():
        return padverb[random.randint(0,len(padverb)-1)]    
def verb():
        return pverb[random.randint(0,len(pverb)-1)]   
def no():
        return pnoun[random.randint(0,len([pnoun])-1)]



def customsentence():
    noun=n()
    return det()+" "+adj()+" "+prep()+" "+noun+" "+v_tr()+" "+pro()+" "+noun+" "+v_itr()
    

def customsentence2():
    ad=adverb()
    if ad!="non":
       return verb()+" "+n()+" "+ad
    else:
        return verb()+" "+n()


with open('presentences3.csv', 'w+') as f_object:
   field_names = ['IsFromCustomer','Text','index']
   dictwriter_object = DictWriter(f_object, fieldnames=field_names)
   dictwriter_object.writeheader()
   for _ in range(1000):
       dict={'IsFromCustomer':False,'Text':customsentence2(),'index':0} 
       print(dict)
       dictwriter_object.writerow(dict)
  
   f_object.close()

