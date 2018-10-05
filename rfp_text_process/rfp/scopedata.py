import pdftotext,os,json
import sys,re,requests
reload(sys)
sys.setdefaultencoding( "utf-8" )
if not os.path.exists("./ALL_TOC"):
     os.makedirs("./ALL_TOC")

dirs=os.listdir("./ALL_PARSE")
for files in dirs:
    #print files
    f=open("./ALL_PARSE/"+files,"r")
    r=f.read()
    f.close()
    data=r.split("\n")
    dict_list={}
    c=0
    for x in data:
         c+=1
         dict_list[c]=x
         if re.search(r'scope',x,re.IGNORECASE):
              x
    #print dict_list
    # f=open("./ALL_SCOPE/"+files,"w")
    # for line in dict_list:
    #      f.write(str(line)+","+str(dict_list[line])+"\n")
    #      print line,dict_list[line]
    # f.close()
    
    #f=open("./ALL_SCOPE/"+files,"w")
    tablecontent={}
    for line in dict_list:
         #print line,dict_list[line]
         #dict_list[line]
         if re.search(r'\d+$',dict_list[line]):
              match=re.search(r'\d+$',dict_list[line])
              Particulars=re.sub(match.group(),"",dict_list[line])
              Particulars = re.sub('\.\.+ ?', ' ',Particulars) 
              #print dict_list[line],match.group()
              #print Particulars.strip(),match.group()
              tablecontent[Particulars]=match.group()
              #mydtict={}
              #mydtict[Particulars]=match.group()
              f=open("./ALL_TOC/"+files+".csv","a")
              f.write(str(Particulars)+","+str(match.group())+"\n")
              #json.dump(mydtict,f)
              #f.close()
              #f.write("{")
              #f.write("'"+str(Particulars)+"':'"+str(match.group())+"'")
              #f.write("}")
              #f.write(",")
              f.close()
    #for key,value in tablecontent:
    #     print key.ljust(50), value.ljust(60)
    print "{:<8} {:<15}".format('Key','label')
    for k, v in sorted(tablecontent.iteritems()):
         label=v
         print "{:<8} {:<15}".format(k, label)
         # #f.write(str(line)+","+str(dict_list[line])+"\n")
         # #print line,dict_list[line]
         # checknext=0
         # if re.search(r'scope|project scope|scope of work',dict_list[line],re.IGNORECASE):
         #      #print  dict_list[line]
         #      checknext=line
              
         # if checknext>0:
         #      checknex



              
              #print dict_list[checknext]
              #print checknext,"Page_no____________________"
              #`f.close()
    # for line in dict_list:
    #      if re.search(r'([0-9.]{1,2}\s+[a-zA-Z ]+[.]{2,}\s?[0-9]\s?[-]?[0-9]?)',dict_list[line],re.IGNORECASE):
    #           print dict_list[line]
    #           break

    # List=""
    # for x in data:
    #     if re.search('([0-9.]{1,2}\s+[a-zA-Z ]+[.]{2,}\s?[0-9]\s?[-]?[0-9]?)',x,re.IGNORECASE):
    #         #match=re.search('([0-9]{1,2}\s+[a-zA-Z ]+[.]{2,}\s?[0-9]\s?[-]?[0-9]?)',x,re.IGNORECASE).group()
    #         #print match
    #         print x
    #         List=List+x+"\n"
    #     elif re.search('([0-9]{1,2}\s+([a-zA-Z ]+[0-9]-?[0-9]?))',x,re.IGNORECASE):
    #         #match=re.search('([0-9]{1,2}\s+([a-zA-Z ]+[0-9]-?[0-9]?))',x,re.IGNORECASE).group()
    #         #print match
    #         List=List+x+"\n"

    # f=open("./ALL_PARSE/"+files,"a")
    # f.write(str(List))
    # f.close()
    
    
            
