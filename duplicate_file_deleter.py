import os;
import hashlib;
from collections import defaultdict
LIST_OF_FILES =[]
FILE_HASH_DICTIONARY = {}
duplicates = []
Test = []

def dubs():
    LIST_OF_FILES =os.listdir('HERE') #-----------------CHANGE
    for f in LIST_OF_FILES:
        p = 'HERE' #-----------------CHANGE - must append / to end of path
        p = p+f
        if os.path.isfile(p):
            Test.append(p)
    for file in Test:
        hash(str(file))


def hash(file):
    BLOCKSIZE = 65536
    hasher = hashlib.sha1()
    with open(file, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    FILE_HASH_DICTIONARY[file] = hasher.hexdigest()


def deal_with_dubs():
    hash_to_names = defaultdict(list)
    #copies = [] ---> sometimes python needs copies to be declared, so if you get an error, just uncomment here
    for name, hash_k in FILE_HASH_DICTIONARY.items():
        hash_to_names[hash_k].append(name)
        copies = []
        for names in hash_to_names.values():
            if len(names) > 1:
                names.sort()
                copies.append(names)
    for n in copies: duplicates.append(n)

def delete_copies():
    print("original: ", duplicates)
    for n in duplicates:
        del n[0]
    print("Removing the following duplicate files: ", duplicates)
    for n in duplicates:
        for i in n:
            os.remove(str(i))

if __name__ == '__main__':
    dubs()
    #print(FILE_HASH_DICTIONARY)
    deal_with_dubs()
    delete_copies()
    print(os.listdir('HERE')) #-----------------CHANGE


