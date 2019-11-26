#function returning square of numbers in a list

def squared(numbers):
    """without generators"""
    result = []
    for number in numbers:
        result.append(number*number)
    return result

def squared_with_generator(numbers):
    """with generators"""
    for number in numbers:
        yield number*number

squared_numbers = squared([1, 2, 3, 4, 5])
squared_numbers_gen = squared_with_generator([1, 2, 3, 4, 5])

##aplying list comprehgension
list_numbers = [number*number for number in [1, 2, 3, 4, 5]]

#generator
list_numbers_gen = list(number*number for number in [1, 2, 3, 4, 5])

#type casting gens into list however compromises perfomance
for number in squared_numbers_gen:
    print(number)