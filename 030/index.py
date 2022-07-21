fruits = ["Apple", "Pear", "Orange"]

def makePie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("FruitPie")
    else:
        print(fruit + "pie")



makePie(4)