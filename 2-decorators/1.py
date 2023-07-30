def Decorator(function):
    
    def wrapper():
        print("iam decorating your function")
        function()
    
    return wrapper

def helloWorld():
    print("hello world")


# direct calling
Decorator(helloWorld)()


# storing the func
newFunc = Decorator(helloWorld)
newFunc()


