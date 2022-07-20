firstList = [int(line.strip()) for line in open("file1.txt")]
secondList = [int(line.strip()) for line in open("file2.txt")]

print(firstList)
print(secondList) 

finalList = [n for n in firstList if secondList.count(n) > 0]

print(f"The overlapping data is : {finalList}")