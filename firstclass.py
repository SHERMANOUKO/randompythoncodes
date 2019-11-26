def square(x):
    return x * x

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

def log(logtype):
    def msg(msg):
        print("logged msg {} of type {}".format(logtype, msg))

    return msg

squared = my_map(square, [1, 2, 3])
cubed = my_map(cube, [1, 2, 3])

# print(squared, cubed)

x = log(1)
x("bad error")
print(x.__name__)
