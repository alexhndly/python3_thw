# Printing, Printing

#assign variable formatter to a string with 4 spaces for inputted values 
formatter = "{} {} {} {}"

#calls format function inside print to match the values into the {}'s in the formatter string
print(formatter.format(1, 2, 3, 4))

#works with strings too
print(formatter.format("one", "two", "three", "four"))

#and Boolens it ignores the fifth variable
print(formatter.format(True, False, False, True, True))

#inputs itself into the string similar to multiplying by 4
print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
    "Try your",
    "own text here.",
    "Maybe a poem",
    "or a reference to beer",
    "This does not print!"
))