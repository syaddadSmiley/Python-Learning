x = int(input())

for i in range(x):
    y = input().strip()
    name = "Bob"
    if y[-1] in "AEIOUaeiou":
        name = "Alice"
    elif y[-1] in "Yy":
        name = "nobody"
    print("Case #" + str(i + 1) + ":", y, "is ruled by", name + ".")