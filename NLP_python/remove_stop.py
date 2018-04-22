import os
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
dirs=os.listdir("./input")
stop_words = set(stopwords.words('english'))
for files in dirs:
    print files
    f=open("./input/"+files,"r")
    line=f.read()
    f.close()
    words = line.split()
    for r in words:
        if not r in stop_words:
            appendFile = open('out.txt','a')
            appendFile.write(" "+r)
            appendFile.close()
    # sent_tok=sent_tokenize(r)
    # print sent_tok
    
    # #print "Tokenize Words"
    # word_tok=word_tokenize(r)
    # #print word_tok

    # stop_words = set(stopwords.words('english'))
 
    # word_tokens = word_tokenize(word_tok)
 
    # filtered_sentence = [w for w in word_tokens if not w in stop_words]
 
    # filtered_sentence = []
 
    # for w in word_tokens:
    #     if w not in stop_words:
    #         filtered_sentence.append(w)
 
    # print(word_tokens)
    # print(filtered_sentence)

    # f=open("output_sent.txt","w")
    # f.write(sent_tok)
    # f.close()

    # f=open("output_word.txt","w")
    # f.write(word_tok)
    # f.close()
    
