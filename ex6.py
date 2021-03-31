# Strings and Text

# assings 10 to the variable types_of_people and uses that in the fstring assigned to x.
types_of_people = 10
x = f"There are {types_of_people} types of people"

#same as above but for text not an integar
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

#printing a variable that has a string assigned to it
print(x)
print(y)

#printing a fstring that has a variable inside it which happens to also be a string
print(f"If I said: {x}")
print(f"Then I also said: '{y}'")

#setting variable hilarious to boolean value False
hilarious = False
#assigning string to joke_evaluation with {} to add something in
joke_evaluation = "isn't that joke so  funny?! {}"

#printing usinf the format function to place the value of hilarious where th {} is in joke_evaluation
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# using the + opertor to concatenate the strings assigned to variables w and e
print(w + e)


