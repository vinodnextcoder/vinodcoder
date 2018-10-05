import pdftotext,os
import sys,re,requests
reload(sys)
sys.setdefaultencoding( "utf-8" )
if not os.path.exists("./ALL_PARSE"):
     os.makedirs("./ALL_PARSE")

dirs=os.listdir("./ALL_TXT")
for files in dirs:
    print files
    f=open("./ALL_TXT/"+files,"r")
    r=f.read()
    f.close()
    
    data=r.split("\n")
    List=""
    for x in data:
        if re.search('([0-9.]{1,2}\s+[a-zA-Z ]+[.]{2,}\s?[0-9]\s?[-]?[0-9]?)',x,re.IGNORECASE):
            #match=re.search('([0-9]{1,2}\s+[a-zA-Z ]+[.]{2,}\s?[0-9]\s?[-]?[0-9]?)',x,re.IGNORECASE).group()
            #print match
            print x
            List=List+x+"\n"
        elif re.search('([0-9]{1,2}\s+([a-zA-Z ]+[0-9]-?[0-9]?))',x,re.IGNORECASE):
            #match=re.search('([0-9]{1,2}\s+([a-zA-Z ]+[0-9]-?[0-9]?))',x,re.IGNORECASE).group()
            #print match
            List=List+x+"\n"

    f=open("./ALL_PARSE/"+files,"a")
    f.write(str(List))
    f.close()
    
            
