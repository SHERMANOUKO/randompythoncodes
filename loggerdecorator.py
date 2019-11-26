from functools import wraps

def my_logger(orig_func):
    """function logs which argument and function has executed"""
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs)
        )
        return orig_func(*args, **kwargs)
    
    return wrapper


def my_timer(orig_func):
    """function times code execution time of a function"""
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    
    return wrapper

@my_timer
@my_logger
def display_info(name, age):
    print("I am called {} and i am {} years old".format(name, age))

display_info('Sherman', 25)