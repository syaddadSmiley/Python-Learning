def rot13(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print("random alphabet (a-z, A-Z, 0-9) : ")
    print("you can shuffle the alphabet ")
    ran_alphabet = input(" : ")

    change = dict(zip(alphabet, ran_alphabet))
    return ''.join(change.get(char, char) for char in phrase)

def ROT13(phrase):
    key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?"
    val = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM6789054321!@#$%^&*()?"
    transform = dict(zip(key, val))
    return ''.join(transform.get(char, char) for char in phrase)

def Rot13(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    result = ""

    for char in phrase:
        result += alphabet[(alphabet.find(char)+18) % 72]
    return result

phrase = input("Phrase : ")

#print(rot13(phrase))
#print(rot13(rot13(phrase)))


print("\n")
print(Rot13(phrase))
print(Rot13(Rot13(Rot13(Rot13(phrase)))))
