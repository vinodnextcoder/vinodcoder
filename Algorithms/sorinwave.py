def sortWave(arr, n):
    # traverse all element
    for i in range(0, n, 2):
        # if current event element smaller then previous
        if i > 0 and arr[i] > arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
        # if current element even smaller than next
        if i < n - 1 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]


arr = [10, 90, 49, 2, 1, 5, 23]
sortWave(arr, len(arr))
print("#############>>>>>>>##################")
for i in range(0, len(arr)):
    print(arr[i]),
