import sys, getopt

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])

print(opts)
print(args)


#> python3 4.py apple.txt "heyllooo"
#> []
#> ['apple.txt', 'heyllooo']

#> python3 4.py -f apple.txt -m "heyllooo"
#> [('-f', 'apple.txt'), ('-m', 'heyllooo')]
#> []

