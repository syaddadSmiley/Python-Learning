name = input("Masukkan Nama : ")
length = int(input("Length : "))
result  = ""

for i in range(len(name)):
    char = name[i]
    if char.isupper():
        result += chr((ord(char) + length - 65) % 26 + 65)
    else:
        result += chr((ord(char) + length - 97) % 26 + 97)

print(result)
