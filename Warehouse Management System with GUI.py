from tkinter import *
from tkinter import messagebox

data = {}

def inputBarang():
    print("@" * 75)
    vName = input("\nNama Barang : ")
    vPrice = input("Harga Barang : ")
    vTotal = int(input("Jumlah Barang : "))
    print('\n')
    data[vName] = {"Harga" : vPrice, "Total" : vTotal}
    messagebox.showinfo('Berhasil!', 'Anda Berhasil Memasukkan Data Barang')

def delBarang():
    print("@" * 75)
    vName = input("Nama Barang yang Keluar : ")
    vTotal = int(input("Jumlah Barang yang Keluar : "))

    try:
        totalAwal = data[vName]['Total']
        totalAkhir = totalAwal - vTotal
        if totalAkhir == 0:
            data[vName]['Total'] = 0
        elif totalAkhir < 0:
            print("Pengeluaran Barang melebihi Stok Barang!\n")
        else:
            data[vName]['Total'] = totalAkhir
        print('Info Barang di Update =>',data[vName],'\n')
    except KeyError:
        print("No Barang Called", vName, '\n')

def showBarang():
    print("@" * 75)
    for nama, info in data.items():
        print("\nNama :", nama)
        for key in info:
            print(key + ':', info[key])

def cariBarang():
    print("@" * 75)
    vName = input("Masukkan Barang yang dicari : ")
    try:
        print(vName,':',data[vName])
    except KeyError:
        print("No Barang Called", vName, '\n')


def editBarang():
    print("@"*75)
    vName = input("Masukkan Nama Barang : ")

    try:
        print(vName,':',data[vName])
        print("Apa yang ingin anda tukar?")
        print("1. Nama\n2.Harga\n3.Keduanya")
        pilih = input("Ingin Menukar yang mana? (1/2/3):  ")
        if pilih == '1':
            v_newName = input("Masukkan Nama Baru : ")
            data[v_newName] = data.pop(vName)
            messagebox.showinfo('Berhasil','Anda Behasil Mengubah Nama Barang')
        elif pilih == '2':
            v_newPrice = input("Masukkan Harga Baru : ")
            data[vName]["Harga"] = v_newPrice
        elif pilih == '3':
            v_newName = input("Masukkan Nama Baru : ")
            v_newPrice = input("Masukkan Harga Baru : ")
            confirm = input("Are u Sure? ((y/n) n default) : ")
            if confirm == 'y':
                data[v_newName] = data.pop(vName)
                data[vName]["Harga"] = v_newPrice
            elif confirm == 'n':
                print("you have canceled the action")
            else:
                print("Wrong input, so we cancel the action")
    except KeyError:
        print("No Barang Called", vName, '\n')


window = Tk()
window.title('Data Gudang')
window.configure(background='white')
window.geometry('500x400')

lblHeading = Label(window, text="Gudang-gudangan", width = 20, font=("bold", 20), bg='white')
lblHeading.place(x=90, y=30)

btn_inp = Button(window, text="Input Barang", command = inputBarang, bg='black', fg='white', font=("bold", 10)).place(x=90, y=100)
btn_del = Button(window, text="Barang Keluar", command = delBarang, bg='black', fg='white', font=("bold", 10)).place(x=90, y=150)
btn_find = Button(window, text="Cari Barang", command = cariBarang, bg='black', fg='white', font=("bold", 10)).place(x=90, y=200)
btn_show = Button(window, text="Tampilkan Semua Barang", command = showBarang, bg='black', fg='white', font=("bold", 10)).place(x=90, y=250)
btn_edit = Button(window, text="Edit Info Barang", command = editBarang, bg='black', fg='white', font=("bold", 10)).place(x=90, y=300)


window.mainloop()