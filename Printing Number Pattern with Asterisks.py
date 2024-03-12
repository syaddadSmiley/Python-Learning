#https://articlearn.id/article/e4536e9b-soal-tes-logika-untuk-masuk-kerja/
n = input()
x = int(n)
for i in range(0,x):
    for j in range(1,x+4):
        if j==i+2:
            print("*", end='')
            continue
        if j==i+3:
            print("*", end='')
            continue
        print(j, end='')
    print(end="\n")