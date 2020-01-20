def pen(arr, n):
    arr.sort(reverse=False)
    # pos stored last index
    pos = n - 1

    if (n % 2 == 0):
        odd = n - 1
    else:
        odd = n - 2
    # move all element to right position

    while odd > 0:
        temp = arr[odd]
        in1 = odd
        # shift element to odd position
        while in1 != pos:
            arr[in1] = arr[in1 + 1]
            in1 += 1
        arr[in1] = temp
        odd = odd - 2
        pos = pos - 1
    # reverse the array el
    start = 0
    end = int((n - 1) / 2)
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

        # Printing the pendulum arrangement
    for i in range(n):
        print(arr[i], end=" ")


arr=[1, 3, -1, 3, 6, 4]
pen(arr, len(arr))
