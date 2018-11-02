'''
Created on Nov 1, 2018

@author: nwijesinha

More code examples using Python
'''

def break_words(stuff):
    ''' This function will break up words'''
    words = stuff.split(' ')
    return words

def sort_words(words):
    # This function sorts words
    return sorted(words)

def print_first_word(words):
    # This function print the first word
    word = words.pop(0)
    print(word)

def print_last_word(words):
    # this function prints the last word
    word = words.pop(-1)
    print(word)
    
def sort_sentence(sentence):
    ''' This function takes a full sentence and returns the sorted sentence'''
    words = break_words(sentence)
    return words

def print_first_and_last(sentence):
    """ This function prints first and last words of a sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """ This function prints the first and last words after sorting the sentence"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    


sentence = "All god things come to those who weight."

words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)

print_last_word(words)

print_first_word(sorted_words)

print_last_word(sorted_words)

sorted_words = sort_sentence(sentence)

print(sorted_words)

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)