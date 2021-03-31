# Parameters, Unpacking, Variables

from sys import argv

#unpacking of argv to 4 variables
script, first, second, third = argv 

print("This script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

correct = input("Is that correct?")

print(correct)