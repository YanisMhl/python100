def cypher(string, key, encrypting):
    result = ""
    for char in string:
        if encrypting:
            result += chr(ord(char) + key)
        else:
            result += chr(ord(char) - key)
    return result


#Initialisation
message = input("Give a message to encrypte : ")
key = int(input("Give a key to go with : "))

#Function call
encryptedMessage = cypher(message, key, True)
decryptedMessage = cypher(encryptedMessage, key, False)

#Display
print(f"Your encrypted message : {encryptedMessage}")
print(f"Your decrypted message : {decryptedMessage}")
