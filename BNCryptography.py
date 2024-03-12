# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
global key 
key = "abcdefghijklmnopqrstuvwxyz1234567890:/?.,"
def main():
    print("Encrpyt / Decrypt / Show All (1/2/3) : ")
    menu = int(input())
    if menu == 1:
        global arr
        arr = []
        print("Input Plains Text : ")
        raw_text = input()
        for i in raw_text:
            arr.append(i)
        encrypt()
    elif menu == 2:
        print("Input Chiper Text : ")
        chiper_string_raw = input()
        print(decrypt(chiper_string_raw))
    elif menu == 3:
        ShowAllList()
    else:
        print("Wrong Input!")
        main()

def ShowAllList():
    file_name = open("linkMyBruh.txt", "r")
    manyLine = file_name.readlines()
    count = 0
    for i in manyLine:
        count += 1
        x = decrypt(i)
        print("Line {} : {}".format(count, x.strip()))

def Convert(string):
    global list1
    list1 = []
    list1[:0] = string
    return list1

def encrypt():
    global arr_chiper
    arr_chiper = []
    Convert(key)
    for i in arr:
        if i in key:
            for j in range(0, len(list1)):
                if i == list1[j]:
                    try:
                        arr_chiper.append(list1[j+5]+"BN")
                    except(IndexError) as E:
                        # print(list1[j])
                        if list1[j] == ":":
                            arr_chiper.append("a"+"BN")
                        elif list1[j] == "/":
                            arr_chiper.append("b"+"BN")
                        elif list1[j] == "?":
                            arr_chiper.append("c"+"BN")
                        elif list1[j] == ".":
                            arr_chiper.append("d"+"BN")
                        elif list1[j] == ",":
                            arr_chiper.append("e"+"BN")
        else:
            arr_chiper.append(i)


    listToStr = ''.join([str(elem) for elem in arr_chiper])
    print(listToStr)
    addToFile(listToStr)

def addToFile(str):
    file_name = "linkMyBruh.txt"
    try:
        f = open(file_name, 'a')
    except FileNotFoundError:
        f = open(file_name, 'w')
    finally:
        f.write('\n'+str)
        print("===========================")
        print("=== Successfully Added! ===")
        print("===========================")

def decrypt(chiper_string_raw):
    Convert(key)
    global arr_text
    arr_text = []
    # print("Input Chiper Text : ")
    # chiper_string_raw = input()
    chiper_string = chiper_string_raw.replace("BN", "")
    for i in chiper_string:
        if i in key:
            for j in range(0, len(list1)):
                if i == list1[j]:
                    try:
                        arr_text.append(list1[j-5])
                    except(IndexError):
                        print(list1[j])
                        if list1[j] == 'e':
                            arr_text.append(',')
                        elif list1[j] == 'd':
                            arr_text.append('.')
                        elif list1[j] == 'c':
                            arr_text.append('?')
                        elif list1[j] == 'b':
                            arr_text.append('/')
                        elif list1[j] == 'a':
                            arr_text.append(':')
        else:
            arr_text.append(i)

    listToStr = ''.join([str(elem) for elem in arr_text])
    return listToStr

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()