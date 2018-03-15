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


mark_rank = {}

for k, v in dict1.items():
    mark_rank[v] = mark_rank.get(v, [])
    mark_rank[v].append(k)
f=open("Rank_output.csv","a")
f.write("User_id"+","+"Mark"+","+"Rank"+"\n")
f.close()
rank_count=0
for key, value in mark_rank.items():
    rank_count+=1
    f=open("Rank_output.csv","a")
    for x in value:
        f.write(str(x)+","+str(key)+","+str(rank_count)+"\n")
    f.close()
