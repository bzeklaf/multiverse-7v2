import re

from difflib import SequenceMatcher
import difflib
import nltk
from nltk.tokenize import sent_tokenize
#nltk.download('punkt')


def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()

#anticipation 
def anticipation_func(body_of_text):
    small_dictionary = {'Item 1 found':['Item 1'], 'Item 2 found':['Item 2']}
    # body_of_text = 'Here is the large body of text. Each sentence in this body, should be compared to each of the values in the dictionary. If the comparision ration is above certain treshold, corresponding key should be printed.'
    sentencing = sent_tokenize(body_of_text)
    list_of_keys = []
    for key,value in small_dictionary.items():
        for item in value:
            for token in sentencing:
                resulting = similar(item,token)
                if resulting >= 1:
                    list_of_keys.append(key)
    if(len(list_of_keys)>0):
        list_of_keys = set(list_of_keys)
    return list_of_keys

#anti_anticiption
def anti_anticipation(body_of_text):
    small_dictionary = {'Item 1 not found':['Item 1'], 'Item 2 not found':['Item 2']}
    sentencing = sent_tokenize(body_of_text)
    list_of_keys = []
    
    for key,value in small_dictionary.items():
        
        for item in value:
            found_value = 0
            for token in sentencing:
                resulting = similar(item,token)
                
                if resulting >=0.9:
                    found_value = 1
                    continue
                    
                    
            if found_value == 0:
                list_of_keys.append(key)
    list_of_keys = set(list_of_keys)
    return list_of_keys

#CW
def cw_processing(text):
    wording = text
    a = {'Item 1 found':['Item 1', 'Similar Item 1', 'Another Similar Item 1']}
    for key,value in a.items():
        for item in value:
            if item in wording:
                yield(key)
                break
    b = {'Item 1 not found':['Item 1'], 'Item 2 not found':['Item 2']}
    for key,value in b.items():
        for item in value:
            if item not in wording:
                yield(key)
                break   
#REGEX
def reg_pro(text):
    patterns = [r'Item 1', r'Item 2']
    rs=['Response to Item 1', 'Response to Item 2']
    wording = text
    little_box = []
    for pattern in patterns:
        #print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')
        if re.search(pattern, wording):
            #print('found a match!')
            little_box.append((rs[patterns.index(pattern)]))
    return(little_box)
       
#APP
def appoint_processing(text):
   wording = text
   a = {'Item 1 found':['Item 1', 'Similar Item 1', 'Another Similar Item 1']}
   for key,value in a.items():
       for item in value:
           if item in wording:
               yield (key)
               break
   b = {'Item 1 not found':['Item 1'], 'Item 2 not found':['Item 2']}
   for key,value in b.items():
       for item in value:
           if item not in wording:
               yield (key)
               break 

#def regular(text):
#    wording = text
#    pattern = re.compile(r'[1-5]')#values beetween 1-5 
#    matches = pattern.finditer(wording)#extra functionality of a match object
#    for match in matches:
#        yield(match)
    
