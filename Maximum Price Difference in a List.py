harga = [10, 7, 5, 8, 11, 9 ,1]
def selisih(x):
    t = 0
    dari = 0
    ke = 0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] > x[j]:
                continue
            if t < x[j]-x[i]:
                t = x[j] - x[i]
                dari = x[i]
                ke = x[j]
    print(dari ,"->", ke)
    return  t

print(selisih(harga))