def myfunc(myparameter: int):
    print(myparameter)

# myfunc("hlier")

# python3 1.py
#> hlier

#> pip3 install mypy
#> 
#> 
#> mypy main.py
#> 
#> 1.py:4: error: Argument 1 to "myfunc" has incompatible type "str"; expected "int"  [arg-type]
#> Found 1 error in 1 file (checked 1 source file)


#> if all are correct:
#> mypy 1.py
#> Success: no issues found in 1 source file


#> pyton is still dynamically typed language:
#> mypy helps in type checking

def myfunc2(myp: int) -> str:
    print("sdfsdf")
    return "hello"
    # return 1

x = myfunc2(77)