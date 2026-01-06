def get_even_numbers_count(numbers):
    even_count = 0
    numbers = numbers.split()
    
    for number in numbers:
        number = int(number)
        if number % 2 == 0:
            even_count += 1
    return even_count


numbers = input()
result = get_even_numbers_count(numbers)
print(result)