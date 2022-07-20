import pandas 
word = input("Enter a word: ").upper()

natoData = pandas.read_csv("nato_phonetic_alphabet.csv")
phoneticDict = {row.letter: row.code for (index, row) in natoData.iterrows()}
result = [phoneticDict[letter] for letter in word]
print(result)