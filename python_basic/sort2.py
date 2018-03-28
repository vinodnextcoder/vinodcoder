List=[3,1,5,2,0,3]
for i in range(len(List)):
    m=i
    for j in range(i+1,len(List)):
        if List[m]>List[i]:
            m=j
    List[i],List[m]=List[m],List[i]
print List
