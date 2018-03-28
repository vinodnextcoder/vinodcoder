
arr = [4, 4, 1, 3, 2, 50, 6]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
 

 

print "List sorted" 
print arr
