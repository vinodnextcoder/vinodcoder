def rverseList(List, start, end):
    while (start < end):
        temp = List[start]
        List[start] = List[end]
        List[end] = temp
        start += 1
        end = end-1
 

List= [1, 2, 3, 4, 5, 6, 7]
n = len(List)
print "List Before Reverse"
for i in range(0, len(List)):
        print List[i],
rverseList(List, 0, n-1)
print "List After Reverse"
for i in range(0, len(List)):
        print List[i],

