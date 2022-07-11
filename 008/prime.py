def isPrime(number):
    result = True
    for i in range(2, number):
        if number % i == 0:
            result = False 
    return result 

n = int(input("Give a number : "))

if isPrime(n):
    print("It's a prime number.")
else:
    print("It's not a prime number.")