def addNumbers(*args):
    result = 0
    for n in args:
        result += n 
    return result 

print(addNumbers(1, 2, 3))

#def calculate(**kwargs):
    