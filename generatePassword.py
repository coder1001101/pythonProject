import random
import string 
letters = string.ascii_letters
num = '1234567890'
spe = '_-/#.?!@+""'':,=![]{}()<>&%|\~`€¥£$¢αβ^* '
symbols = letters + num + spe
length = int(input("Enter Password Length : "))
pass1 = "".join(random.sample(symbols, length))
print("Your new password is : ", pass1)
print("*******************************")

newpass1 = pass1.replace('a', 'M')
newpass2 = pass1.replace('b', 'N')
newpass3 = pass1.replace('c', 'O')
newpass4 = pass1.replace('d', 'P')
newpass5 = pass1.replace('e', 'Q')
newpass6 = pass1.replace('f', 'R')
newpass7 = pass1.replace('g', 'S')
newpass8 = pass1.replace('h', 'T')
newpass9 = pass1.replace('i', 'U')
newpass0 = pass1.replace('j', 'V')
newpass11 = pass1.replace('k', 'W')
newpass12 = pass1.replace('l', 'X')
newpass13 = pass1.replace('m', 'Y')
newpass14 = pass1.replace('n', 'Z')
newpass3 = pass1.replace('o', 'A')
newpass3 = pass1.replace('p', 'B')
newpass3 = pass1.replace('q', 'C')
newpass3 = pass1.replace('r', 'D')
newpass3 = pass1.replace('s', 'E')
newpass3 = pass1.replace('t', 'F')
newpass3 = pass1.replace('u', 'G')
newpass3 = pass1.replace('v', 'H')
newpass3 = pass1.replace('w', 'I')
newpass3 = pass1.replace('x', 'J')
newpass3 = pass1.replace('y', 'K')
newpass3 = pass1.replace('z', 'L')
print(f"New password with replace is : \t{newpass1} \n {newpass2} \n {newpass3}")

print(f"1: \t{newpass1}\n2:\t{newpass2}")