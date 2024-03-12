bob_lst = [3,4,6,10,11,15]
alice_lst = [1,5,8,12,14,19]

def merge_list(bob, alice):
    bobal = []
    for i in range(0, len(bob)):
        bobal.append(bob[i])
        bobal.append(alice[i])
    for j in range(0, len(bobal)):
        for z in range(0, len(bobal)):
            if bobal[j] < bobal[z]:
                temp = bobal[j]
                bobal[j] = bobal[z]
                bobal[z] = temp
    return bobal

print(merge_list(bob_lst, alice_lst))