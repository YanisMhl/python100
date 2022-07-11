print('''                             
                               ("O_)
                              / `-/
                             /-. /
                            /   )
                           /   /  
              _           /-. /
             (_)"-._     /   )
               "-._ "-'""( )/    
                   "-/"-._" `. 
                    /     "-.'._
                   /\       /-._"-._
    _,---...__    /  ) _,-"/    "-(_)
___<__(|) _   ""-/  / /   /
 '  `----' ""-.   \/ /   /
               )  ] /   /
       ____..-'   //   /                       )
   ,-""      __.,'/   /   ___                 /,
  /    ,--""/  / /   /,-""   """-.          ,'/
 [    (    /  / /   /  ,.---,_   `._   _,-','
  \    `-./  / /   /  /       `-._  """ ,-'
   `-._  /  / /   /_,'            ""--"
       "/  / /   /"         
       /  / /   /
      /  / /   /  
     /  |,'   /  
    :   /    /
    [  /   ,'  
    | /  ,'
    |/,-'
    ''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
firstChoice = input("left or right ?")
if firstChoice == "left":
    secondChoice = input("swim or wait ?")
    if secondChoice == "wait":
        thirdChoice = input("Which door ?")
        if thirdChoice == "Yellow":
            print("You Win !")
        elif thirdChoice == "Red":
            print("Burned by fire.\nGame Over.")
        elif thirdChoice == "Blue":
            print("Eaten by beasts.\nGame Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")