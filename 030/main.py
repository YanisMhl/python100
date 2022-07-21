#FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["rgregr"])
# except FileNotFoundError:
#     file = open('a_file.txt', "w")
#     file.write("something")
# except KeyError as errorMessage:
#     print(f"The key {errorMessage} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up")
#     #file.close()
#     #print("File was closed.")

#KeyError
#a_dictionary = {"key": "value"}
#value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters")

bmi = round(weight / height**2, 2)

print(bmi)