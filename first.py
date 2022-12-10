from datetime import datetime

def prime_first(n:int):
    number_of_primes = n
    for i in range(1,n+1):
        for j in range(2,i):
            if i%j == 0:
                number_of_primes -= 1
                break
    # 1 is not prime!
    number_of_primes -= 1
    
    return number_of_primes

def prime_first_not_optimal(n:int):
    number_of_primes = n
    for i in range(1,n+1):
        prime = True
        for j in range(2,i):
            if i%j == 0 and prime is True:
                prime = False
                number_of_primes -= 1
                
    # 1 is not prime!
    number_of_primes -= 1
    
    return number_of_primes


# basic test of the functions

# now = datetime.now()
# print(prime_first(10000))
# print("Optical : " + str(datetime.now() - now))


# now = datetime.now()
# print(prime_first(20000))
# print("Optical : " + str(datetime.now() - now))

# now = datetime.now()
# print(prime_first_not_optimal(100))
# print("Not Optical : " + str(datetime.now() - now))