def pr(arr, size):
    for i in range (0, size):
        for j in range (i + 1, size):
            if arr[i] == arr[j]:
                print arr[i]
     
# Driver code
List = [4, 2, 4, 5, 2, 3, 1]
n = len(List)
pr(List,n)
 
