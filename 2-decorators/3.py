# Doing it in better way would be 
def mydecorator(function):
    
    def wrapper(*args, **kwargs):
        print("iam decorating your function")
        function(*args, **kwargs)
    
    return wrapper

@mydecorator
def hello(person):
    print(f"hello {person}")


hello("harshi")



