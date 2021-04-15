# Names, Variables, Code, Fucntions

#like scripts with argv
def print_two(*args):
    arg1, arg2 = args #unpacking args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}") #no need for unpacking as set as indepandant parameters

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I've got nothin'")

print_two("alex", "wwfc")
print_two_again("alex", "wwfc")
print_one("alex")
print_none()
