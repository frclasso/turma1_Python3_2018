class myIterator:
    a = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > 10: raise StopIteration
        self.a += 1
        return self.a


iter = myIterator()
for i in iter:
    print(i, end=', ')