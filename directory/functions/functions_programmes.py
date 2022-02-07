''' wap to print "hai everyone" if on arguments is given by the user '''


# def input_(a='Hai everyone'):
#     print(a)
#
#
# input_('anisu tide yako indu , neene ne nanavale yendu, mayada loka didnda, nangagi bandavandu')
#
#
# input_()

''' wap to check weather a number is prime or not '''


# def prime_(num:int):
#
#     for i in range(2, num-1):
#         if num % i == 0:
#             return num, 'not a prime'
#     return num, 'is a prime no'
#
#
# print(prime_(7))

''' wap to return last digit of a number '''

# def last_num(a:int):

    # b = str(a)
    # return int(b[-1])
#     return (a % 10)
#
# print(last_num(50253215124801))

''' waf name tail takes a sequence as input and a number n and returns the last n elements from the sequence '''


# def name_tail(n: int, sequence):
#
#     return sequence[-n:]
#
#
# print(name_tail(2, 'hello'))

#''' waf named is_perfectsquare that accepts a no and returns true if  it is perfectsquare and return false if it is not'''


# def is_perfect_square(num):

    # sq_rt = int(num ** 0.5)
    # if sq_rt * sq_rt == num:
    #     return True
    # return False

#     for i in range(num):
#         if i * i == num:
#             return True
#     return False
#
#
# print(is_perfect_square(27))


# def per_sq_rng(r1: int):
#
#     l = []
#     i = 1
#     while i <= r1:
#         r = int(i ** 0.5)
#         #i += 1
#         if r * r == i:
#             l.append(i)
#     return l


''' assignment for loop -strings'''

print(per_sq_rng(500))


''' waf to return the below output
func("TRACXN", 0) >>> RCN
func("TRACXN", 1) >>> TAX
 '''


# def func(string, inte):
#     l = []
#     for i in string[inte::2]:
#         l.append(i)
#     return l
#
#
# print(func('TRACXN', 0))
# print(func('TRACXN', 1))

''' waf to that checks if the given number is a fibonacci number or not '''


# def fibo(num):
#     a = 0
#     b = 1
#     l = []
#     for _ in range(num):
#         if a <= num:
#             l.append(a)
#             c = a + b
#             a = b
#             b = c
#         if num in l:
#             return f'{num} is a fibonacci number'
#
#     return f'{num} is not a fibonacci number'
#
#
# print(fibo(35))


''' waf to that takes variable no of inputs and returns length of all the iterables given '''

# a = [1,2,3,4,5,6,7,8,9]
# s = 'euphoria'
# t = ('dinga', 'dingi', 'manga')
#
#
# def len_iter(*args):
#     d = {}
#     for i in args:
#         if isinstance(i, (str, list, tuple, set, dict)):
#             d[len(i)] = i
#     return d
#
#
# print(len_iter(a,s,t,1,'hello',3,'asma',5))

