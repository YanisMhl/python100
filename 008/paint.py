import math 

def canNumber(height, width, coverage):
    return math.ceil((height*width)/coverage) 


h = int(input("What's the height of your wall ? "))
w = int(input("What's the width of your wall ? "))
c = int(input("What's the coverage of your cans ? "))

number = canNumber(h, w, c)

print(f"The number of cans you need is : {number}")