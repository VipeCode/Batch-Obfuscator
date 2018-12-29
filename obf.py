import random


def obfuscate(code):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    alpha = ''.join(random.sample(alphabet, len(alphabet)))
    new = "@echo off\nSet _var=" + alpha + "\ncls\n"

    for c in code:
        if c in alpha:
            new = new + "%_var:~" + str(alpha.find(c)) + ",1%";
        else:
            new = new + c

    return new

f = open("file.bat", "r")
print(obfuscate(f.read()))