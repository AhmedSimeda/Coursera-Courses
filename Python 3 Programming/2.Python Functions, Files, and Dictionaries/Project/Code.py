#!/usr/bin/env python
# coding: utf-8

# In[ ]:


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
# a function to remove the unwanted marks from a word
def strip_punctuation(word):
    for punc in punctuation_chars:
        word = word.replace(punc,'')
    
    return word

# a function that counts the positive words in the given sentence(s)
def get_pos(string):
    #getting a list of all the words
    string = string.split()
    n_pos = 0                # my accumulator variable
    for word in string:
        word = strip_punctuation(word).lower()
        if word in positive_words:
            n_pos += 1
    
    return n_pos

# a function that counts the negative words in the given sentence(s)
def get_neg(string):
    #getting a list of all the words
    string = string.split()
    n_neg = 0                # my accumulator variable
    for word in string:
        word = strip_punctuation(word).lower()
        if word in negative_words:
            n_neg += 1
    
    return n_neg

#let's open our csv file and write our resulting data at the same time
#in order to use less memory :)
first_line = True                                #a flag the first line
file = open('project_twitter_data.csv','r')
resulting_data = open('resulting_data.csv','w')

for line in file:
    if first_line:  #will work only at the first line :)
        #let's put our headers
        resulting_data.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
        first_line = False   #thank you, you did your job. Goodbye now :)
        continue
    #strip() for removing '\n' and split(',') to get each item separately 
    txt,retweets,replies = line.strip().split(',')
    n_pos = get_pos(txt)
    n_neg = get_neg(txt)
    net   = n_pos - n_neg
    #let's add them now to our resulting_data file
    resulting_data.write('{},{},{},{},{}\n'.format(retweets,replies,str(n_pos),str(n_neg),str(net)))

#Don't forget to close what you've opened :)
file.close()                  
resulting_data.close()

