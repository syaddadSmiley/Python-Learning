x = int(input())

for t in range(x):
    papers = int(input())
    citations = list(map(int, input().strip().split()))

    print(f"Case #{t + 1}:", end=" ")

    for n in range(1, papers + 1):
        count = [0] * (n + 2)
        for i in range(n):
            if citations[i] > n:
                count[n + 1] += 1
            else:
                count[citations[i]] += 1

        total = count[n + 1]
        index = 0

        for i in range(n, -1, -1):
            total += count[i]
            if total >= i:
                index = i
                break
        print(index, end=" ")
    print()