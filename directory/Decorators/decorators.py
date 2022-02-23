""" wa decorator that logs a message before executing any function """


""" wa decorator which takes a string and reverse it """


# def rev(func):
#     def wrapper(*args, **kwargs):
#         print('reversed string : ')
#         res = func(*args, **kwargs)
#         return func
#     return wrapper
#
#
# @rev
# def rev_str(string):
#
#     return string[::-1]
#
#
# print(rev_str('shallo'))

""" wa decorator to execute a function for three times """


# def repeat_(func):
#     def wraper(*args, **kwargs):
#         for i in range(3):
#             func(*args, **kwargs)
#
#     return wraper
#
#
# @repeat_
# def display(string):
#     print(string)
#
#
# display('hai')

""" wa decorator which inputs a delay of n seconds """
import time


# def outer(n):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(n)
#             func(*args, **kwargs)
#         return wrapper
#     return delay


# @outer(3)
# def add(a, b):
#     print(a + b)


# add(5, 4)

""" wa decorator to calculate the time of execution of a function """


# def outer():
#     def time_(func):
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             func(*args, **kwargs)
#             end = time.time()
#             print('Time of execution is ', [end-start])
#         return wrapper
#     return time_
#
#
# a = [1,2,3,4,5,6,7,8,9]
# s = 'euphoria'
# t = ('dinga', 'dingi', 'manga')
#
#
# @outer()
# def len_iter(*args):
#     d = {}
#     for i in args:
#         if isinstance(i, (str, list, tuple, set, dict)):
#             d[len(i)] = i
#     return d


# len_iter(a,s,t,1,'hello',3,'asma',5)


""" wa decorator to count the number of arguments passed to a function """


def count_(func):
    def wrapper(*args, **kwargs):
        count = 0
        res =func(*args, **kwargs)

        for i in args:
            count += 1
        for j in kwargs:
            count += 1

        print(count)
    return wrapper


@count_
def coll(*args,**kwargs):
    return args, kwargs


a = 1,23,2,6
coll(a, 2, 33, 5, 48, 6, b=10)


""" wadf to return only positive values after subtraction """


def posit(func):
    def wrapper(*args, **kwargs):
        res = abs(func(*args, **kwargs))
        return res
    return wrapper


@posit
def sub(a, b):
    return (a-b)


print(sub(1, 10))

""" wadf to print hello world if no input is given by user """


def inpu(func):
    def wrapper(*args, **kwargs):

        res = func(*args, **kwargs)
        return res

    return wrapper


@inpu
def inp(string='hello world'):
    print(string)


inp('nooooo!')
inp()


"""wadf to return the length of the given iterable """


def length_(func):
    def wrapper(*args, **kwargs):
        count = 0
        res = func(*args, **kwargs)
        for i in res:
            count += 1

        return count
    return wrapper

@length_
def itera(a):
    return a


print(itera('ninidale sadda badukudu ee dina'))


""" wadf to print hello world if no input is given by user  using parameter decorator"""


def outer(s='hello world'):
    def input_(func):
        def wrapper(*args, **kwargs):
            res = func(*args, *kwargs)
            if len(res) == 0:
                res = s

            return res
        return wrapper
    return input_


@outer('p')
def inp(a=''):
    return a


print(inp('whyyyy???'))
print(inp())

help(setattr)