List=[1,1,2,3,1,3]

List_C=[0]*len(List)
Counter={}
for i,v in enumerate(List):
    if v in Counter:
        Counter[v]+=1
    else:
        Counter[v]=0

    List_C[i]=Counter[v]

print Counter
