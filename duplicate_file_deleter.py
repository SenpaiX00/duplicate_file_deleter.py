import os;
import shutil;
import hashlib;

LIST_OF_FILES =[]
FILE_HASH_DICTIONARY = {}
copies = []

def dubs():
    LIST_OF_FILES =os.listdir('/Users/simoaugu/PycharmProjects/untitled')
    #print("\n".join(files))
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
        hash(str(file))


def hash(file):
    BLOCKSIZE = 65536
    hasher = hashlib.sha1()
    with open(file, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    #print(file, hasher.hexdigest())
    FILE_HASH_DICTIONARY[file] = hasher.hexdigest()

def deal_with_dubs():
    count = 0
    files_to_compare = FILE_HASH_DICTIONARY.copy()
    print ('files ',files_to_compare)
    for file in FILE_HASH_DICTIONARY:
        print(file, FILE_HASH_DICTIONARY[file])
        for file1 in files_to_compare:
            if str(FILE_HASH_DICTIONARY[file]) == str(files_to_compare[file1]):
                count = count+1
        if count ==1 : count = 0
        print count
        if count > 1:
            copies.append(str(file))
            count = 0
    #print copies

def delete_copies():
    

if __name__ == '__main__':
    dubs()
    #print(FILE_HASH_DICTIONARY)
    deal_with_dubs()
