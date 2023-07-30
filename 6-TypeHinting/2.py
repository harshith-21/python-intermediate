def myfunc(mytparameter: int) -> str:
    return f"{mytparameter + 10}"

def otherfunc(otherparaneter: str):
    print(otherparaneter)

otherfunc(myfunc(20))


def myfunc2(mytparameter: int) -> int:
    return mytparameter + 10

def otherfunc2(otherparaneter: str):
    print(otherparaneter)

otherfunc2(myfunc2(20))