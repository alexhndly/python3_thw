# Reading Files

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
# calling the read() function on the txt variable, no parameters set beacuse of (), read is part of open
print(txt.read())
# line 7 creates a file object rather than tha actual file so it's good to close() when finished with.
txt.close()

print("Type the filename again:")
file_again = input('>>> ')

txt_again = open(filename)

print(txt_again.read())
txt_again.close()

