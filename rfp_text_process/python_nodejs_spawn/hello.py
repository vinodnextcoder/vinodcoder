import sys ,re
# Takes first name and last name via command  
# line arguments and then display them 
print("Output from Python") 
print("First name: " + sys.argv[1]) 
print("Last name: " + sys.argv[2])

f=open(sys.argv[1],"r")
r=f.read()
f.close()    
data=r.split("\n")
#data=data.replace("&"," ")
List=""
for x in data:
    x=x.replace(r"&","")
    #x=re.sub(r'&',"",x,re.IGNORECASE)
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
     if re.search(r'scope',x,re.IGNORECASE):
          x

tablecontent={}
for line in dict_list:
     if re.search(r'\d+$',dict_list[line]):
          match=re.search(r'\d+$',dict_list[line])
          Particulars=re.sub(match.group(),"",dict_list[line])
          Particulars = re.sub('\.\.+ ?', ' ',Particulars)
          Particulars=re.sub(r'(page\s?[0-9]\sof\s)',"",Particulars,re.IGNORECASE)
          tablecontent[Particulars]=match.group()
          print Particulars,match.group()
          f=open("1test.csv","a")
          f.write(str(Particulars)+","+str(match.group())+"\n")
          f.close()
