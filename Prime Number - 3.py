def is_prime(number):
    no_of_factors = 0
    for i in range(1, number + 1):
        if (number % i == 0):
            no_of_factors += 1
            
    if no_of_factors == 2:
        return "Prime Number"
    else:
        return "Not a Prime Number"


number = int(input())
result = is_prime(number)
print(result)