"""
Program by Kristian Lonergan
Student Number: C12321971
Date: 12/12/2013

TASKS
We are going to do some simple analysis on this.
1. Count the number of words in the speech. We will exclude from our analysis a number of 'stop words', in our example 
these will be the definite and indefinite articles and some personal pronouns.
2. Count the unique words in the collection produced by 1 above.
3. Count the number of occurrences of each word.
"""

import string
import urllib.request
#----------FUNCTIONS----------#

"""This function is cutting the line down into to words
and converting the words form uppercase to lowercase
so we can add words to the dictionary"""

def process_line(line,word_count_dict,seperator):
    line = line.strip()
    word_list = line.split(seperator)
    """processes the line to get lowercase words and add to dictionary """
    for word in word_list:
        word = word.lower()
        word = word.strip(string.punctuation)#gets rid of commas periods etc.
        add_word(word,word_count_dict)#calls function add_word
        

"""This Function is adding words to the dictionary and
if they are already in the dictionary they're incremented by one"""

def add_word(word,word_count_dict):
    
    if word in word_count_dict:#if word is in dict, then increment it
        word_count_dict[word] += 1
    else:#if word is not in dict, initialise it to 1
        word_count_dict[word] = 1

#This function which prints neatly the number of word occurances        
def printWord(word_count_dict):
    #creates a list of tuples
    value_key_list = []
    
    for key,val in word_count_dict.items():
        value_key_list.append((val,key))
        
    value_key_list.sort(reverse = True)#Gets highest to lowest
    print('-'*21)#print '-' out 21 times
    print('{:11s}{:11s}'.format('Word','Count'))
    print('-'*21)
    for val,key in value_key_list:
        print('{:12s}{:<5}'.format(key,val))


#----------MAIN----------#

#declaring empty dictionary
word_count_dict = {}
stopCount = {}

#reading from test file
speech = open('gettysburg.txt','r')
stopWords = open('stopwords.txt','r')

seperator = ','
for line in stopWords:
    process_line(line,stopCount,seperator)

seperator = ' '
"""The seperators are different for the two files so i pass through
the specified seperator for each"""

#Basically reads the whole file (paragraph) and goes to function process line
for line in speech:
    process_line(line,word_count_dict,seperator)
counter = 0

#This is getting the number of words in the whole file
for value in word_count_dict.values():
    counter = counter + value

print("Number of words excluding the stopwords",(counter)-len(stopCount))    
print("Number of unique words excluding the stopwords:",((len(word_count_dict)-(len(stopCount)))))#This subtracts    
print("Number of Unique words:",len(word_count_dict))

#This calls the function which prints neatly the number of occurances
printWord(word_count_dict)
