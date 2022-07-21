import pandas 

natoData = pandas.read_csv("nato_phonetic_alphabet.csv")
phoneticDict = {row.letter: row.code for (index, row) in natoData.iterrows()}
print(phoneticDict)

word = input("Enter a word: ").upper()
result = [phoneticDict[letter] for letter in word]
print(result)