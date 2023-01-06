class Function:
    def __init__(self, call, *args, **kwargs):
        self.call = call
        self.args = args
        print(self.args)
        self.kwargs = kwargs

    def __call__(self, *x, **y):
        return self.call(*self.args, **self.kwargs)
