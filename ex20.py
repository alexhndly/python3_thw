# Functions and Files

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read()) #f has read called on it to print out the contents of f

def rewind(f):
    f.seek(0) #moves the file to byte 0

def print_a_line(line_count, f):
    print(line_count, f.readline()) #takes in two arguments, on it just passes to print and the other has readline called on it
    #readline read until the byte after a \n and returns it too

current_file = open(input_file) # opes the file input by the user in the CLI and set the variable current_file

print("First let's print the whole file:\n")

print_all(current_file) #print the file by calling the print_all function

print("Now let's rewind, kind of like a tape:")

rewind(current_file) #sets the open file back to the first byte using rewind function if this isn't donw the next bit will print blank as the read head is at the EOF

print("Let's print three lines:")

current_line = 1 #current line value is passed to the function this value does not interact with f.readline() 
print_a_line(current_line, current_file)

current_line = current_line + 1 # current_line += 1 current line is now at value 2 to be passed to print_a_line
print_a_line(current_line, current_file)

current_line = current_line + 1 #currenlt_line value changes again to now be 3
print_a_line(current_line, current_file)

