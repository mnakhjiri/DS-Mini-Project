import math


def second_prime(n:int):
    number_of_primes = n
    for i in range(1,n+1):
        for j in range(2,int(math.sqrt(i))+1):
            if i%j == 0:
                number_of_primes -= 1
                break
    # 1 is not prime!
    number_of_primes -= 1
    
    return number_of_primes

def second_prime_not_optimal(n:int):
    number_of_primes = n
    for i in range(1,n+1):
        prime = True
        for j in range(2,int(math.sqrt(i))+1):
            if i%j == 0 and prime is True:
                prime = False
                number_of_primes -= 1
    # 1 is not prime!
    number_of_primes -= 1
    
    return number_of_primes
    