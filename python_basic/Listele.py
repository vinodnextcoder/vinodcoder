# Python Program - One Dimensional Array

while True:
    print("Enter 'e' for exit.")
    nval = input("How many element you want to store in the array ? ")
    if nval == 'e':
        break
    else:
        n = int(nval)
        arr = []
        for i in range(1, n+1):
            arr.append(i)
        print("\nElements in Array are:")
        for i in range(0, n):
            print(arr[i], end=" ")
        print("\n")
