auctions = {}
highestBid = 0
winner = ""
gameOn = True


print("Welcome to the secret auction program.")

while gameOn:
    name = input("What is your name? : ")
    bid = int(input("What's your bid?: $"))
    auctions[name] = bid
    otherBidders = input("Are there any other bidders? Type 'yes' or 'no' : ")

    if otherBidders == 'no':
        gameOn = False 
        

for key in auctions:
    if auctions[key] > highestBid:
        highestBid = auctions[key]
        winner = key
        
print(f"The winner is {winner} with a bid of ${highestBid}")
        


    