#!/usr/bin/env python3
# We can XOR integers by first converting the integer from decimal to binary.
# We can XOR strings by first converting each character to the integer representing the Unicode character.

from operator import xor

### Sample XOR
a = bool(1)
b = bool(0)
print(a^b)

# integer from decimal to binary: 13
def decimalToBinary(n):
    return "{0:b}".format(int(n))

if __name__ == '__main__':
    print(decimalToBinary(13))

# String Conversion to binary: label
# Ascii codes found online
# print("The binary for 'label' is... " decimalToBinary(1089798101108))
print(decimalToBinary(108))
print(decimalToBinary(97))
print(decimalToBinary(98))
print(decimalToBinary(101))
print(decimalToBinary(108))

# word = ['l', 'a', 'b', 'e', 'l']
for x in "label":
    print(decimalToBinary(x))

string = 'label'
[ord(c) for c in string]
