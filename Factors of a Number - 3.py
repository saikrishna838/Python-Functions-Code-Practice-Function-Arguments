def factors_of_n(number):
    factors = []
    
    for each_num in range(1, number + 1):
        if number % each_num == 0:
            factors += [str(each_num)]
            
    factors_separated_by_space = " ".join(factors)
    return factors_separated_by_space
    
number = int(input())
result = factors_of_n(number)
print(result)