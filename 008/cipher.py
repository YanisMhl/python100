def encrypte(string, key):
    result = ""
    for char in string:
        result += chr(ord(char) + key)
    return result

def decrypte(string, key):
    result = ""
    for char in string:
        result += chr(ord(char) - key)
    return result

message = input("Give a message to encrypte : ")
key = int(input("Give a key to go with : "))

encryptedMessage = encrypte(message, key)

print(f"Your encrypted message : {encryptedMessage}")

decryptedMessage = decrypte(encryptedMessage, key)

print(f"Your decrypted message : {decryptedMessage}")
