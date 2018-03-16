import csv
fields = []
rows = []
dict1={}
with open('marks_list.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
 
    for row in csvreader:
        if not row[1] in rows:
            rows.append(row[1])
        dict1[row[0]]=row[1]
print set(dict1.values())
List=[]
for i in set(dict1.values()):
    List.append(int(i))
#print sorted(List)
f=open("Output.csv","a")
f.write("User_id"+","+"Mark"+","+"Rank"+"\n")
f.close()
dict2={}
c=0
List= sorted(List)
for i in range(len(List)-1,0,-1):
    c+=1
    for k, v in dict1.items():
        if List[i]==int(v):
            f=open("Output.csv","a")
            f.write(str(k)+","+str(v)+","+str(c)+"\n")
            f.close()
        
            

#for row in rows:
#    print row
# mark_rank = {}
# c=0
# for r in rows:
#     for k, v in dict1.items():
#         if v==r :
            
#             mark_rank[k] =1
#         else:
#             print r,v
#             mark_rank[k] = 2
# for k, v in mark_rank.items():
#     print k,v
            
