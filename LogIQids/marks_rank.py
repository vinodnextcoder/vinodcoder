import csv
fields = []
rows = []
dict1={}
with open('marks_list.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
 
    for row in csvreader:
        rows.append(row[1])
        dict1[row[0]]=row[1]


result = {}
c=0
for key,value in dict1.items():
    if value in result.values():
        result[key] = [value]
    else:
        result[key].append(value)

#print result
# for r in rows:

#     for k, v in dict1.items():
        
#         if v==r :
#             mark_rank[k]= +1
#         else:
#             mark_rank[k]=1
        
for k, v in result.items():
     print k,"   " ,v
