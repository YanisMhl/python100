guests = [] 
newFiles = []
newLetters = []

with open("invitedNames.txt") as file:
    rawGuests = file.readlines()
    
    for guest in rawGuests:
        guests.append(guest.strip())
    

with open("startingLetter.txt") as file:
    letterFile = file.read()
    for guest in guests:
        newFile = guest + "Letter.txt"
        newFiles.append(newFile)
        newLetter = letterFile.replace("[name]", guest)
        newLetters.append(newLetter)
 

for i in range(0, len(guests)):
    with open(newFiles[i], mode="w") as invitation:
        invitation.write(newLetters[i])            
        
        