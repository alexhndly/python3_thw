# More Variables and Printing

name = 'Alex'
age = 28 # not a lie
height = 71 # inches
weight = 154 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

weight_in_kg = weight * 0.453592
height_in_cm = height * 2.54

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"Which is {height_in_cm}cm.")
print(f"He's {weight} pounds heavy.")
print(f"Which is {weight_in_kg}kg.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height} and {weight} I get {total}.")