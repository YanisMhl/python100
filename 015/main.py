import data 

def displayReport(m):
    for key in m:
        if key == 'water' or key == 'milk':
            print(f"{key}: {m[key]}ml")
        elif key == "coffee":
            print(f"{key}: {m[key]}g")
        else:            
            print(f"{key}: ${m[key]}")
            
def changeMachine(mach, cof):
    mach["water"] -= cof["water"]
    mach["milk"] -= cof["milk"]
    mach["coffee"] -= cof["coffee"]
    mach["money"] += cof["price"]
    
def sorryEmpty(mach, cof):
    if cof["water"] > mach["water"]:
        print("Sorry, there's not enough water.")
    elif cof["milk"] > mach["milk"]:
        print("Sorry, there is not enough milk.")
    elif cof["coffee"] > mach["coffee"]:
        print("Sorry, there's not enough coffee.")
        
def enough(mach, cof):
    result = True
    if cof["water"] > mach["water"]:
        result = False
    elif cof["milk"] > mach["milk"]:
        result = False
    elif cof["coffee"] > mach["coffee"]:
        result = False
    return result
        
def findCoffee(name, list):
    result = {}
    for i in range(0, len(list)):
        if list[i]["name"] == name:
            result = list[i]
    return result

def calculateChange(quarter, dime, nickle, penny):
    return quarter*0.25+dime*0.10+nickle*0.05+penny*0.01

#initialize machine
machine = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

choice = ""

while choice != "nothing":
    
    choice = input("What would you like? (espresso/latte/cappuccino):")
    
    
    if choice == "report":
        displayReport(machine)
        
        
    elif choice == "espresso":
        coffee = findCoffee("espresso", data.coffees)
        
        if enough(machine, coffee):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            money = round(calculateChange(quarters, dimes, nickles, pennies), 2)
            
            if money > coffee["price"]:
                change = round(money - coffee["price"], 2)
                print(f"Here is ${change} in change.")
                print("Here is your espresso. Enjoy !") 
                changeMachine(machine, coffee)
                
            elif money == coffee["price"]:
                print("Here is your espresso. Enjoy !") 
                changeMachine(machine, coffee)
                
            else:
                print("You don't have enough money. Please try again.")
        else:
            sorryEmpty(machine, coffee)
    
    elif choice == "latte":
        coffee = findCoffee("latte", data.coffees)
        
        if enough(machine, coffee):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            money = round(calculateChange(quarters, dimes, nickles, pennies), 2)
            
            if money > coffee["price"]:
                change = round(money - coffee["price"], 2)
                print(f"Here is ${change} in change.")
                print("Here is your latte. Enjoy !") 
                changeMachine(machine, coffee)
                
            elif money == coffee["price"]:
                print("Here is your latte. Enjoy !") 
                changeMachine(machine, coffee)
                
            else:
                print("You don't have enough money. Please try again.")
        else:
            sorryEmpty(machine, coffee)
            
            
            
    elif choice == "cappuccino":
        coffee = findCoffee("cappuccino", data.coffees)
        
        if enough(machine, coffee):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            money = round(calculateChange(quarters, dimes, nickles, pennies), 2)
            
            if money > coffee["price"]:
                change = round(money - coffee["price"], 2)
                print(f"Here is ${change} in change.")
                print("Here is your cappuccino. Enjoy !") 
                changeMachine(machine, coffee)
                
            elif money == coffee["price"]:
                print("Here is your cappuccino. Enjoy !") 
                changeMachine(machine, coffee)
                
            else:
                print("You don't have enough money. Please try again.")
        else:
            sorryEmpty(machine, coffee)
    
    elif choice == "nothing":
        print("Ok ! Bye !!")
    else:
        print("Wrong choice. Please try again.")
            
            
            
        
        