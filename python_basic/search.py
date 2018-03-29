List=[1,2,4,5,7,3,9,1]
List1=[0 for i in range(len(List))]
cnt=[0 for i in range(256)]
for i in range(len(List)):
    cnt[i]+=1
for i in range(len(List)):
    List1[cnt[List[i]]-1]=List[i]
    cnt[List[i]]-=1
print List1
