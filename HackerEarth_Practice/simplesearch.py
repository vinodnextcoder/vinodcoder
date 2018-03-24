n = int(input())
List=[int(i) for i in input().split()]
k = int(input())
     
for i in range(len(List)):
     if List[i]==k:
         print (i)
         break
