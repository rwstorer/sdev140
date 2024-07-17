import pickle

class myClass(object):
    CLASS_VAR: int = 1
    def __init__(self):
        self.var = 2

class myClass2(myClass):
    def __init__(self):
        super().__init__()
        self.var2 = 2

m = myClass()
m2 = myClass2()
print(m2.CLASS_VAR)
m.CLASS_VAR = 2
print(m2.CLASS_VAR)


def write_dictionary():
    my_dictionary: dict = {}
    my_dictionary['one']=1
    my_dictionary['two']=2
    my_dictionary['three']=3
    my_dictionary['four']=4

    f = open('file.txt', 'wb')
    pickle.dump(my_dictionary, f)
    f.close()

def read_dictionary():
    myd: dict = []
    f = open('file.txt', 'rb')
    myd = pickle.load(f)
    print(myd)
    f.close()
