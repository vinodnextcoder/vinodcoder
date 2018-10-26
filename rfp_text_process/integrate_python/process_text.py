# -*- coding: utf-8 -*-                                                                                                                      
import sys ,re,json,os,sys,pdftotext
from pymongo import MongoClient
reload(sys)
sys.setdefaultencoding( "utf-8" )

fp=sys.argv[1]
f=open(fp, "r")
pdf = pdftotext.PDF(f)
f.close()
fp1=fp.replace(".pdf",".txt")
print fp1
for i in range(1,5):
    f=open(fp1,"a")
    f.write(str(pdf[i]))
    f.close()
    
f=open(fp1,"r")
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
#print List
data=List.split("\n")
dict_list={}
c=0
for x in data:   
    c+=1
    dict_list[c]=x
jsonname=fp1
jsonname=jsonname.replace(".txt",".json")
jsonname=jsonname.replace("./","")
List2=[]
tablecontent={}
f=open(jsonname,"w")
f.write("{")
c=0
for line in dict_list:    
   if re.search(r'(([0-9]{1,}\s?-\s?[0-9]{2,})|(\d+$))',dict_list[line]):
      c+=1
      match=re.search(r'(([0-9]{1,}\s?-\s?[0-9]{2,})|(\d+$))',dict_list[line])
      Particulars=re.sub(r'(([0-9]{1,}-[0-9]{2,})|(\d+$))',"",dict_list[line])
      Particulars = re.sub('\.\.+ ?', ' ',Particulars)
      Particulars=re.sub(r'(page\s?[0-9]\sof\s)',"",Particulars,re.IGNORECASE)
      tablecontent[Particulars]=match.group()
      #print Particulars,match.group()
      f.write('"'+str(Particulars).strip()+'":"'+str(match.group())+'",')
f.write("}\n")
f.close()
projectscope={}
for line in dict_list:
    if re.search(r'(([0-9]{1,}\s?-\s?[0-9]{2,})|(\d+$))',dict_list[line]):
        match=re.search(r'(([0-9]{1,}\s?-\s?[0-9]{2,})|(\d+$))',dict_list[line])
        Particulars=re.sub(r'(([0-9]{1,}-[0-9]{2,})|(\d+$))',"",dict_list[line])
        Particulars = re.sub('\.\.+ ?', ' ',Particulars)
        Particulars=re.sub(r'(page\s?[0-9]\sof\s)',"",Particulars,re.IGNORECASE)
        tablecontent[Particulars]=match.group()
    if re.search(r'Scope',dict_list[line],re.IGNORECASE):
        if re.search(r'(([0-9]{1,}\s?-\s?[0-9]{2,})|(\d+$))',dict_list[line]):
            match=re.search(r'(([0-9]{1,}\s?-\s?[0-9]{2,})|(\d+$))',dict_list[line])
            Particulars=re.sub(r'(([0-9]{1,}-[0-9]{2,})|(\d+$))',"",dict_list[line])
            Particulars = re.sub('\.\.+ ?', ' ',Particulars)
            Particulars=re.sub(r'(page\s?[0-9]\sof\s)',"",Particulars,re.IGNORECASE)
            print Particulars,match.group(),"printcode"
            projectscope[Particulars]=match.group()
        NO=""
        if re.search(r'(^\d)',Particulars,re.IGNORECASE):
            NO = re.search(r'(^\d)',Particulars,re.IGNORECASE).group()
        if re.search(NO,dict_list[line]):
            dict_list[line]
        if re.search(r'(([0-9]{1,}\s?-\s?[0-9]{2,})|(\d+$))',dict_list[line+1]):
            match=re.search(r'(([0-9]{1,}\s?-\s?[0-9]{2,})|(\d+$))',dict_list[line+1])
            Particulars=re.sub(r'(([0-9]{1,}-[0-9]{2,})|(\d+$))',"",dict_list[line+1])
            Particulars = re.sub('\.\.+ ?', ' ',Particulars)
            Particulars=re.sub(r'(page\s?[0-9]\sof\s)',"",Particulars,re.IGNORECASE)
            print Particulars,match.group()
            projectscope[Particulars.strip()]=match.group().strip()
            break

print projectscope
db="projectscope_"+jsonname
print db
# print c,"____counter___"
#f=open(jsonname,"r")
#rr=f.read()
#f.close()
#data=rr.replace(",}","}")
# f=open("xxxxxxxxxxxxxxxxx.json","w")
# f.write(json.dump(projectscope))
# f.close()
with open(db, 'w') as outfile:
    json.dump(projectscope, outfile)
db = db.replace(" ","\ ")
command = "mongoimport --db priceBidMain --collection "+db+" --file "+db
print command
# #au print command
output = os.system(command)
