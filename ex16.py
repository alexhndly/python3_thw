# Reading and Writing files

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("I you do want that, hit RETURN")

input("?")

# create object 'target' to call below functions on 
print("Opening the file...")
target = open(filename, 'w')

# #empty the file. we don't need this as the 'w' parameter in open overwrites with write()
# print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I'm going to ask you for three lines.")

# user input three lines
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to file.")

#write inputted lines to the file
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

one_write = f"{line1}\n{line2}\n{line3}\n"

target.write(one_write)

print("And finally, we close it.")
target.close()