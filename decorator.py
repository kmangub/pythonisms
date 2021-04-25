from functools import wraps

def greeting_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return f'Hello there, {original_val}'
    return wrapper
    
def farewell_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return f'Well, {original_val}, It\'s been real. Take care!'
    return wrapper

@greeting_decorator
def name(txt):
    return txt

@farewell_decorator
def nickname(txt):
    return txt


if __name__ == "__main__":
    print(name('Karlo'))

