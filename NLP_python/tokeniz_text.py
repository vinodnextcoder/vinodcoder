import os
import nltk
from nltk.tokenize import sent_tokenize
dirs=os.listdir("./input")

for files in dirs:
    print files
    f=open("./input/"+files,"r")
    r=f.read()
    f.close()
    #print r
    #Tokenizing text is important since text  be processed without tokenization. Tokenization process means splitting bigger parts to small parts.
    sent_tok=sent_tokenize(r)
    print sent_tok
