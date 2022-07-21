import pandas 

natoData = pandas.read_csv("nato_phonetic_alphabet.csv")
phoneticDict = {row.letter: row.code for (index, row) in natoData.iterrows()}
print(phoneticDict)

def generatePhonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [phoneticDict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        generatePhonetic()
    else:
        print(result)

generatePhonetic()

