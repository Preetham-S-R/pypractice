''' wap to print list of even numbers from list  '''

l = [0,1,2,3,4,5,6,7,8,9,10]

evens = lambda num: num if num % 2 == 0 else None
print(list(filter(evens, l)))

''' wap that returns list of strings with odd length '''

s = ' iss se zyaada tuje aur cha hu to kya ?'

# odd_len = lambda stri: None if len(stri) % 2 == 0 else stri
odd_len1 = lambda string: len(string) % 2 != 0
# print(list(filter(odd_len, s.split())))
print(list(filter(odd_len1, s.split())))

''' wap to which returns all the strings starting with vowels in the given sentence'''

vow = lambda word: word[0] in 'aeiouAEIOU'

print(list(filter(vow, s.split())))

''' wap to the output in the form of individual list of each element '''

s = ' is s se zyaada tuje aur cha hu to kya ?'

res = list(map(list, s.split()))
print(res)

''' wap to get the squares of a list using map '''

l = [1,2,3,4,5,6,7,8,9]

sq = lambda num: num ** 2

print(list(map(sq, l)))

''' wap to print the squares of the even index elements '''

l = [1,2,3,4,5,6,6,7,8,9,9,10,10]

# sq_even = lambda num: (num ** 2) if l.index(num) % 2 == 0 else None

# a = list(map(sq_even, l))



# def p(i):
#     return i


# print(list(filter(p, a)))
#
# res = filter(p, a)
# print(list(res))

