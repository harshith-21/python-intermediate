import sys

thisfilename = sys.argv[0]
filename = sys.argv[1]
message = sys.argv[2]

with open(filename, 'w+') as f:
    f.write(thisfilename, ":",  message)