def myfunc(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])

    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])

# myfunc('hey', 19, True, "wow", KEYONE="TEST", KEYTWO=7)


#will error as we are accessing the that kwarg in the func but we have not passed it
myfunc('hey', 19, True, "wow", KEYTWO=7)

