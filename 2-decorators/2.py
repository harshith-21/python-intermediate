# Doing it in better way would be 
def mydecorator(function):
    
    def wrapper():
        print("iam decorating your function")
        function()
    
    return wrapper

@mydecorator
def helloWorld():
    print("hello world")

helloWorld()



