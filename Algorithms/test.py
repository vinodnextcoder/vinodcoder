from typing import List


def reaarange(arr, n):
    i = -1
    # arrra divide array to elment
    for j in range(n):
        i = +1
        if arr[j] < 0:
            arr[i], arr[j] = arr[j], arr[i]
    print(arr)

    pos, neg = i + 1, 0
    while pos < n and neg < pos and arr[neg] < 0:
        print(arr[neg])
        print (">>>>>>>>>>>>>>")
        arr[neg], arr[pos] = arr[pos], arr[neg]
        pos += 1
        neg + 2

    return arr


arr: List[int] = [1, 2, -3, -5]
test = reaarange(arr, len(arr))
print(test, "")
