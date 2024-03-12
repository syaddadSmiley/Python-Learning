arr = [1,7,3,4]
temp1 = 0
temp2 = 0
temp3 = 0
n = int(input())
if n == 1 or n == 2:
    print(1)
elif n == 3:
    print(3)
elif n < 0:
    print()
else:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                continue
            if arr[i] + arr[j] > n:
                continue
            if arr[i] + arr[j] <= n:
                if arr[i] + arr[j] > temp3:
                    temp3 = arr[i] + arr[j]
                    temp1 = arr[i]
                    temp2 = arr[j]
    print(temp1, "dan", temp2)