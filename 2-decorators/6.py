#timing of a func
import time

def timed(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = function(*args, **kwargs)
        end = time.time()
        fname = function.__name__
        print(f"{fname} took {end-start} time to execute !")
        return value
    return wrapper


@timed
def myfunc(x):
    res = 1
    for i in range(1, x):
        res *= i
    return res

print(myfunc(100))


myfunc(10000)