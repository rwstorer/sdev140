class MultiPass:
    def __init__(self, **kwargs):
        self.var1 = kwargs['var1']
        if (kwargs['var2']):
            pass


def multi_pass(somvar, **kwargs):
    kwargs['var1']
    kwargs['var2']

multi_pass(1, var1=1, var2=2, var3="three")
