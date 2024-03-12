import pyperclip
def main():
    pesan = input("What's ur messages sir? :\n")
    key = 3
    enkripsi = transposition(key, pesan)

    print("Enkripsi : ")
    print(enkripsi +'| ')
    pyperclip.copy(enkripsi)

def transposition(key, pesan):
    enkripsi = ['']*key

    for kolom in range(key):
        position = kolom
        while position < len(pesan):
            enkripsi[kolom] += pesan[position]
            position += key
    return ''.join(enkripsi)
if __name__ == '__main__':
    main()