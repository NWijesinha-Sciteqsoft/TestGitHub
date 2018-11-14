'''
Created on Nov 13, 2018

@author: nwijesinha

Learning Object Oriented using Python

'''

import random
from urllib.request import urlopen 
import sys
from click._compat import raw_input


WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "Class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "Class %%%(object):\n\tdef _init_(self, ***)" :
        "class %%% has-a _init_ Tha takes self and *** parameters.",
    "Class %%%(object):\n|tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instacne of class %%%.",
    "***.***(@@@)":
        "From *** get the ** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From ** get the ** attribute and set it to '***'."
    }

# Do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# load up the wors from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())
    
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                  random.sample(WORDS, snippet.count("%%%"))]
    
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
    
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(','.join(random.sample(WORDS, param_count))).decode('utf-8')
        
    for sentence in snippet, phrase:
        result = sentence[:]
        
        # fake class names
        for word in class_names:
            result = result.replace("%%%", word.decode('utf-8'), 1)
            
        # fake other name
        for word in other_names:
            result = result.replace("***", word.decode('utf-8'), 1)
        
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word.decode('utf-8'), 1)
            
        results.append(result)
    
    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
        
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question 
            
            print(question)
            
            raw_input("> ")
            print("ANSWER: %s\n\n" % answer)

except EOFError:
    print("\nBye")                