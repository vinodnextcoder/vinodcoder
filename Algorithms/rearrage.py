def rearrangeNaive(arr, n):
    # Create an auxiliary array
    # of same size
    temp = [0] * n

    # Store result in temp[]
    for i in range(0, n):
        temp[arr[i]] = i

        # Copy temp back to arr[]
    for i in range(0, n):
        print (temp[i])
        arr[i] = temp[i]

        # A utility function to print
    # contents of arr[0..n-1]


def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")

    # Driver program


arr = [1, 3, 0, 2]
n = len(arr)
rearrangeNaive(arr, n)
# printArray(arr, n)
