"""wacd to return the length of the given iterable """


class count:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


@ count
def length(collection):
    return len(collection)


print(length([1,2,3,4,5,6,7,8,9,10]))