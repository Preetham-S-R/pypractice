''' wa recursion prog to print 10 to 1 '''


# def reve_(start, end):
#     if end-1 == start:
#         return
#     print(start)
#     reve_(start-1, end)
#
#
#
# reve_(10, 1)
#
# # OR
#
#
# def count_down(start, end):
#     if start < end :
#         return
#     print(start)
#     count_down(start-1, end)


''' wa recursion prog to add the digits of a number '''

# n = 123
# s = 0
# while n > 0:
#
#     a = n % 10
#     s += a
#     b = n // 10
#     n = b
#
# print(s)


# def sum_dig(num, sum=0):
#
#     if num > 0:
#         last = num % 10
#         sum += last
#         num = num // 10
#         return sum_dig(num, sum)   # if we don't use return here, the sum will be returned to previous caller i.e it will go back to the first iteration only and will provide the same as result.
#
#     return sum
#
#
# print(sum_dig(123))

''' warp to find the sum of first n numbers '''

# def sum_n(n, sum=0):
#     if n > 0:
#         sum += n
#         return sum_n(n-1, sum)
#     return sum
#
#
# print(sum_n(10))


''' warp to find the factorial of a number '''

# def facto(f, pro=1):
#     if f > 0:
#         pro *= f
#         return facto(f-1, pro)
#     return pro
#
#
# print(facto(5))


''' warp to count the no of digits in a number '''


# def count_dig(num, count1=0):
#
#     if num > 0:
#
#         count1 += 1
#         num = num // 10
#         return count_dig(num, count1)
#     return count1
#
#
# print(count_dig(10))


''' wap to reverse a string '''


def rev_str(s, i=0, s1=''):
    if len(s) > i:
        s1 = s[i] + s1
        return rev_str(s, i+1, s1)
    return s1

print(rev_str('hello'))

''' warp to print fibonacci series upto n but less than 1000 '''


def fibo(upto,a=0,b=1,c=0,):
    if upto > a:
        c = a + b
        b = c
        a = b
        return fibo(upto,a,)
