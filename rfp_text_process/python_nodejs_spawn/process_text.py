# -*- coding: utf-8 -*-                                                                                                                      
import sys ,re,json,os,sys
from pymongo import MongoClient
reload(sys)
sys.setdefaultencoding( "utf-8" )

# Takes first name and last name via command  
# line arguments and then display them
#print("Output from Python") 
#print("File name: " + sys.argv[1]) 
#print("Second parameter name: " + sys.argv[2])

f=open(sys.argv[1],"r")
r=f.read()
f.close()
data=r.split("\n")
List=""
for x in data:
   x = re.sub('\(', '',x)
   x = re.sub('\)', '',x)
   x = re.sub('\,', '',x)
   x = re.sub('\/', '',x)
   x = re.sub('-', '',x)
   x = re.sub(':', '',x)
   x = re.sub('–', '',x)
   if re.search('([0-9.]{1,2}\s+[a-zA-Z ]+[.]{2,}\s?[0-9]\s?[-]?[0-9]?)',x,re.IGNORECASE):
      x=re.sub(r'(Page\s+[0-9]+\sof\s[0-9]{2,})',"",x,re.IGNORECASE)
      #match=re.search('([0-9]{1,2}\s+[a-zA-Z ]+[.]{2,}\s?[0-9]\s?[-]?[0-9]?)',x,re.IGNORECASE).group()
      #print match
      List=List+x+"\n"
   elif re.search('([0-9]{1,2}\s+([a-zA-Z ]+[0-9]-?[0-9]?))',x,re.IGNORECASE):
      x=re.sub(r'(Page\s+[0-9]+\sof\s[0-9]{2,})',"",x,re.IGNORECASE)
      #match=re.search('([0-9]{1,2}\s+([a-zA-Z ]+[0-9]-?[0-9]?))',x,re.IGNORECASE).group()
      #print match
      List=List+x+"\n"
data=List.split("\n")
dict_list={}
c=0
for x in data:   
    c+=1
    dict_list[c]=x
jsonname=sys.argv[1]
jsonname=jsonname.replace(".txt",".json")
jsonname=jsonname.replace("./","")
List2=[]
tablecontent={}
f=open(jsonname,"w")
f.write("{")
for line in dict_list:    
    if re.search(r'(([0-9]{1,}\s?-\s?[0-9]{2,})|(\d+$))',dict_list[line]):
        match=re.search(r'(([0-9]{1,}\s?-\s?[0-9]{2,})|(\d+$))',dict_list[line])
        Particulars=re.sub(r'(([0-9]{1,}-[0-9]{2,})|(\d+$))',"",dict_list[line])
        Particulars = re.sub('\.\.+ ?', ' ',Particulars)
        Particulars=re.sub(r'(page\s?[0-9]\sof\s)',"",Particulars,re.IGNORECASE)
        tablecontent[Particulars]=match.group()
        print Particulars,match.group()
        f.write('"'+str(Particulars).strip()+'":"'+str(match.group())+'",')
f.write("}\n")
f.close()
f=open(jsonname,"r")
rr=f.read()
f.close()
data=rr.replace(",}","}")
f=open(jsonname,"w")
f.write(str(data))
f.close()
jsonname = jsonname.replace(" ","\ ")
command = "mongoimport --db priceBidMain --collection "+jsonname+" --file "+jsonname
# print command
output = os.system(command)
