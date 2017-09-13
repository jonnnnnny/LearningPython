import os

ls = os.linesep
fname = input("input filename: ")
while True:
    if os.path.exists(fname):
        print("ERROR: '%s' already exists", fname)
    else:
        break
print("\nEnter lines('.' by itself to quit). \n")

all = []

while True:
    entry = input(">>")
    if entry == '.':
        break
    else:
        all.append(entry)

fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print("DONE!")