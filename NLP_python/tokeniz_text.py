import os
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
dirs=os.listdir("./input")

for files in dirs:
    print files
    f=open("./input/"+files,"r")
    r=f.read()
    f.close()
    
    sent_tok=sent_tokenize(r)
    print sent_tok
    
    print "Tokenize Words"
    word_tok=word_tokenize(r)
    print word_tok

    f=open("output_sent.txt","w")
    f.write(sent_tok)
    f.close()

    f=open("output_word.txt","w")
    f.write(word_tok)
    f.close()
    
