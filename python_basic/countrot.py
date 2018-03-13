 
List = [45, 23, 12, 10, 22, 98]
n = len(List)
min = List[0]
print "List Elemnts \n"
print List
for i in range(0, n):     
    if (min > List[i]):
        min = List[i]
        min_index = i
print "Min Element",min         



