''' wa lambda function to check weather a given number is even or not '''


even = lambda num: num % 2 == 0


print(even(4))

'''walf that multiplies two numbers '''


product = lambda num1, num2: num1 * num2


print(product(5, 5))

''' walf that returns last element of the sequence '''


last = lambda seq: seq[-1]


print(last('Hello is it me you lookin for ?'))
print(last(['tu', 'tu', 'tu', 'tu', 'meri', 'mai', 'tera', 'honelaga']))

''' walf that checks if the given string is pallindrome or not '''


pallindrome = lambda string: f'{string} is a pallindrome' if string == string[::-1] else ' not pallindrome '


print(pallindrome('dad'))

''' walf to check if a num is even or odd '''

even_odd = lambda num: f'{num} is even' if num % 2 == 0 else f'{num} is odd'

print(even_odd(10))

''' wap that checks if the given list of numbers are even or odd '''

l = [1,2,3,4,5,6,7,8,9,10,11,12,13]

res = map(even_odd, l)
print(list(res))

''' wap to return the strings which are starting with vowels '''

vow = lambda string: f'{string}' if string[0] in 'aeiouAEIOU' else None
print(vow('helo'))

s = 'Hello is it me you lookin for ?'
l1 = s.split()
l2 = ['tu', 'tu', 'tu', 'tu', 'meri', 'mai', 'tera', 'honelaga']
print(list(map(vow, l1)))
print(list(map(vow, l2)))


''' wap to convert all the strings in the list to uppercase using map '''

l = ['apple', 'eat', 'day', 'every','says', 'doctor']


# upper = lambda stri: stri.upper() if isinstance(stri, str) else stri
# print(list(map(upper, l)))

res = map(str.upper, l)
print(list(res))

''' wap to convert all the negative numbers in the list to positive map '''

l = [1,-2,-3,4,-5,-6,7,-8,9,-10]

# posi = lambda inti: abs(inti) if inti < 0 else inti
# print(list(map(posi, l)))

res = map(abs, l)
print(list(res))

''' wap that returns the list of numbers raised to the power of their indices using map '''

l = [1,-2,-3,4,-5,-6,7,-8,9,-10]

power = lambda pow: pow ** l.index(pow)
print(list(map(power, l)))


''' wap that returns all the words in lower case in the give n sentence '''

l = ['APPLE', 'EAT', 'DAY', 'EVERY', 'SAYS', 'DOCTOR']

lower = lambda low: low.lower() if isinstance(low,str) else low
print(list(map(lower, l)))

''' wap to get list of lengths of each word '''

s = 'Hello is it me you lookin for ?'

res = map(len, s.split())
print(list(res))

'''wap to get list of tuples of char and asci '''

s = 'tuje soch ta hu me shaam ho subbha'

asci = lambda i: (i,ord(i))
print(list(map(asci, s)))

''' wap to add teh following list elements simultaneously '''

a = [1,2,3,4]
b = [5,6,7,8]

add = lambda a1, b1: a1 + b1

print(list(map(add,a,b)))






































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































