def prime_third(n:int):
    number_of_primes = 0
    result_array = [True]*n
    for i in range(2,n+1):
        if result_array[i-1] is True:
            for j in range(i*i,n+1,i):
                result_array[j-1] = False
    # 1 is not prime
    result_array[0] = False
    for i in range(1,n+1):
        if result_array[i-1] is True:
            number_of_primes += 1
    return number_of_primes


def prime_fourth(n:int):
    number_of_primes = 0
    result_array = [True]*n
    for i in range(2,n+1):
        for j in range(i*i,n+1,i):
            result_array[j-1] = False
    # 1 is not prime
    result_array[0] = False
    for i in range(1,n+1):
        if result_array[i-1] is True:
            number_of_primes += 1
    return number_of_primes

