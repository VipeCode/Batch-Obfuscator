import random
import numpy as np

def obfuscate(code, sets_num):
    Il = ["I", "l"]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    mixed_alphabet = ''.join(random.sample(alphabet, len(alphabet)))

    alphabets = []
    sets = []
    for x in range(sets_num):
        name = ''.join(random.choices(Il, k=5))
        while name in sets:
            name = ''.join(random.choices(Il, k=5))
        sets.append(name)

    for l in np.array_split(list(mixed_alphabet), sets_num):
        li = []
        for i in l:
            li.append(i)
        alphabets.append(li)

    new = "@echo off\n"
    for x in range(len(sets)):
        new = new + "Set " + sets[x] + "=" + ''.join(alphabets[x]) + "\n"
    new = new + "cls\n\n"

    for c in code:
        last = False
        for x in range(len(alphabets)):
            if c in alphabets[x]:
                if last:
                    new = new[:-1]
                new = new + "%" + sets[x] + ":~" + str(''.join(alphabets[x]).find(c)) + ",1%"
                break
            else:
                if not last:
                    new = new + c
                    last = True

    return new

f = open("file.bat", "r")
print(obfuscate(f.read(), 8))