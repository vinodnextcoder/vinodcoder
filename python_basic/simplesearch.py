n = int(input())
array = [int(i) for i in input().split()]
k = int(input())

for i in range(len(array)):
    if array[i] == k:
        print(i)
        break
