
def printAll(seq):
    if seq:
        print(seq, "->", seq[0])
        printAll(seq[1:])

printAll([1,2,3,4,5])