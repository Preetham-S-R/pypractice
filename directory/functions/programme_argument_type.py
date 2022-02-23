# waf to return the sum of two values

        # ''' we have to give 2 empty lines before after function definition according to convensions '''

''' using both / and *'''


# def add1_(a, /, *, b):
#     c = a + b
#     return c


# print(add1_(5, b=5))

''' using only /'''


# def add2_(a, b, /):
#     c = a + b
#     return c
#
#
# print(add2_(6, 6))

''' using only * '''


# def add3_(*, a , b):
#     c = a + b
#     return c
#
#
# print(add3_(a=7, b=7))


'''waf which returns list even numbers in the range 1-50 '''

# def even_(si, ei):
#     l = []
#     for i in range(si, ei):
#         if i % 2 == 0:
#             l.append(i)
#     return l
#
#
# print(even_(1, 51))


''' creating default value '''

''' waf that returns all the prime numbers in list user defined range if the user dosent provide start index take it as 2 '''


# def prime_(ei, si=2):
#
#     l = []
#     for i in range(si, ei):
#         if i > 1:
#         for j in range(2, i):
#             if i % 2 == 0:
#                 break
#         else:
#             l.append(i)
#     return l
#
#
# print(prime_(50))


''' waf to print fibonacci series in the user defined range '''


# def fibo(r):
#     a = 0
#     b = 1
#     l = []
#     for i in range(r):
#         l.append(a)
#         c = a + b
#         a = b
#         b = c
#
#     return l
#
#
# print(fibo(10))


''' waf that returns fibinacci series upto number specified '''


# def fibo1(upto):
#     a = 0
#     b = 1
#     l = []
#     for i in range(upto):
#         if a <= upto:
#             l.append(a)
#             c = a + b
#             a = b
#             b = c
#         else:
#             break
#     return l
#
#
# print(fibo1(60))


''' waf that returns nth fibonacci number '''


# def fibo2(r1):
#     a = 0
#     b = 1
#     l = []
#     for i in range(r1-1):
#         c = a + b
#         a = b
#         b = c
#     l.append(a)
#     return l
#
# print(fibo2(10))


''' variable positional arguments '''

''' # waf that takes integers and float data type as input or arguments and returns its sum '''


# def sum_(*args):

    #a = sum(args)
    # return a

    # total = 0
    #
    # for i in args:
    #     if isinstance(i,(int, float)):
    #         total += i
    # return total


# print(sum_(1,2,3,1.2,4.5,3.8,0.5))


''' waf  to return the number of positional args that has been given to the function '''


# def pos_(*args):
#
#     # count = 0
#     #
#     # for i in args:
#     #     count += 1
#     # return count
#     return len(args)
#
#
# print(pos_('a',1,2,True,56,'p2',8.0))
#
#
# print(pos_('a'))


''' waf to that takes variable number of positional args and return all the integer values '''


# def inte(*args):

''' waf that takes multiple args and returns the string in reversed order '''

# def rev(*args):
#
#     l = []
#
#     for i in args:
#         if isinstance(i, str):
#             l.append(i[::-1])
#     return l
#
#
# print(rev('apple','ball','call','small', None, True))


''' variable keyword arguments '''

''' waf to that returns no of positional args and no of keyword args '''

# def count_(*args, **kwargs):
#     return len(args), len(kwargs)
#
#
# print(count_(1,2,3,a=10,b=20,c=30))


""" no of args are greater than 5 or not"""


# def great5(*args):
#     if len(args) > 5:
#         return 'args no greater than 5'
#
#     return 'args less than 5'
#
#
# print(great5(0,1,2,3,3,1,32,4,581,6,10,5,85,2,2))
#
#
# print(great5(1,2))
