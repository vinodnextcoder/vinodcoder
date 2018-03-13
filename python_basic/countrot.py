 
List = [15, 18, 2, 3, 6, 12]
n = len(List)
min = List[0]
print List
for i in range(0, n):     
    if (min > List[i]):
        min = List[i]
        min_index = i
print "Min Element",min         



