List=[1,2,1,1,3,5,2,3,5]
List2=[]
for k in set(List):
    List2.append(int(k))
print List
print List2
count = 0
result = 0

for i in List:
    
    if i in List2:
        count += 1
    else:
        if count >= 1:
            result += 1
            count = 0
print count
print(result)
