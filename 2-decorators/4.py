# Doing it in better way would be 
def mydecorator(function):
    
    def wrapper(*args, **kwargs):
        print("iam decorating your function")
        return_value = function(*args, **kwargs)
        return return_value
    
    return wrapper

@mydecorator
def hello(person):
    print(f"hello {person}")
    return f"hello {person}"


print(hello("harshi"))