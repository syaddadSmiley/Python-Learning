import sys
import hashlib
import os

menus = {
    1: "Hash a file",
    2: "Verify a file hash",
    3: "Exit"
}

def hash_file(filename, void=False):
    h = hashlib.sha256()
    with open(filename, 'rb') as file:
        with open(filename+".sha256", 'wb') as hash_file:
            # string_file = str(file.read())
            # hash_file.write(string_file.encode('utf-8'))
            # for byte_block in iter(lambda: file.read(4096), b""):
            #     print(byte_block.decode('utf-8'))
            for byte_block in iter(lambda: file.read(4096), b""):
                h.update(byte_block)
            hash_file.write(h.hexdigest().encode('utf-8'))
        # for byte_block in iter(lambda: file.read(4096), b""):
        #     h.update(byte_block)
    return h.hexdigest()

def verify_hash(filename, hash):
    calculated_hash = hash_file(filename)
    return calculated_hash == hash

def main():
    folder_path = os.path.dirname(os.path.abspath(__file__)) + "./"
    switcher = {
        1: hash_file,
        2: verify_hash,
        3: exit
    }

    sys.stdout.flush()

    choice = int(sys.stdin.readline().strip())
    
    if choice == 3:
        sys.exit(0)
    else:
        filename = folder_path + sys.stdin.readline().strip() 
        hash_input = sys.stdin.readline().strip() #Empty Input if hash_file

        result = switcher[choice](filename, hash_input)
        
        sys.stdout.write(str(result) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()