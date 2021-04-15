# More files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#open in_file and create indata object with contents of the file.
# in_file = open(from_file)
# indata = in_file.read()

#the above can be done in one line LOOK!
indata = open(from_file).read()

#use len to get the length of the input file
print(f"The input file is {len(indata)} bytes long")

#use exists to see if the target file has been creted or not.
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

#opens or creates the target file in write mode.
out_file = open(to_file, 'w')
out_file.write(indata)

# print("Alright, all done.")

out_file.close()
# in_file.close()