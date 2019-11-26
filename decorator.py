def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Executing {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('Wrapper here')
        return self.original_function(*args, **kwargs)


# @decorator_class
# def display():
#     print("display function")


# @decorator_class
# def display_info(name, age):
#     print("I am called {} and i am {} years old".format(name, age))

@decorator_function
def display():
    print("display function")


@decorator_function
def display_info(name, age):
    print("I am called {} and i am {} years old".format(name, age))

# decorated_display = decorator_function(display)

# decorated_display()

display()
display_info('Sherman', 24)
