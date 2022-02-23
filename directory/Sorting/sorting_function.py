s = 'hello'
print(sorted(s))

l = [5,9,7,8,1,3,4,6,7,10,12,90]
print(sorted(l))

set_ = {'hello', 'hai', 'how', 'do', 'do ?'}
print(sorted(set_))

# tup = (1, 2,5,8,10,1,6,'hello', 'beautiful')   ''' sorting not possible in heterogeneous collection '''
# print(sorted(tup))

dict_ = {'a': 8, 'r': 8, 'm': 5}
print(sorted(dict_))

''' sorted() always returns a list '''

#####
''' custom sorting '''

''' wap to sort the elements present in list based on their length '''
s = 'mila hu aab jo tum se'
l = s.split()

print(sorted(l, key=len))


''' wap to find the longest and shortest word in the following string '''

s = ' gulabi aakhen jo teri ddeki sambhalna mushkil hogaya '
l = s.split()

shortest, *rest, longest = sorted(l, key=len)
print(shortest, longest)

''' wap to print shortest and longest word along with their length in the below sentence '''

s = 'samalo mujko oo mere yaro sambalna mushkil hogaya'
l = s.split()

shortest, *rest1, longest = sorted(l, key=len)

print((shortest, len(shortest)), (longest, len(longest)))

''' wap to sort the below list elements based on last character of each string '''

l = ['python', 'java', 'perl', 'c++', 'ruby', 'scooby', 'doo']

print(sorted(l, key=lambda item: item[-1]))

''' wap to sort the below list based on middle character of each element '''

l = ['python', 'java', 'perl', 'c++', 'ruby', 'scooby', 'doo']

print(sorted(l, key=lambda item: len(item) // 2))

'tuje sooch ta hu hu me shamo subha iss se zyada tuje aar chhahu to kya ?'

""" sorting a dictionary using key """

# d = {'gmail': 5, 'walmart': 8, 'apple': 3, 'flipkart': 10}
#
# # ascii
# print(sorted(d))
# print(sorted(d.keys()))
# print(sorted(d.values()))
# print(sorted(d.items()))
#
# # based on len
#
# print(sorted(d, key=len))
# print(sorted(d.keys(),key=len))
#
# # print(sorted(d.values(), key=len))  # not possible
#
# print(sorted(d.items(),key=len))
#
# print(sorted(d.items(), key=lambda items: len(items[0])))
# print(dict(sorted(d.items(),key=lambda items: len(items[0]))))


''' wap to sort a dictionary based on keys last item'''

d = {'gmail': 5, 'walmart': 8, 'apple': 3, 'flipkart': 10}

# print(dict(sorted(d.items(), key=lambda item: item[0][-1])))     #''' use d.items() while sorting dictionary '''

''' wap to sort a dictionary based on values '''

print(dict(sorted(d.items(), key=lambda item: item[-1])))

# print(sorted(d, key=lambda item: d[item]))                        # not to be used

''' wap to sort the above list based on the temparature '''

tempatratures = [('delhi', 32), ('mumbai', 27),('kolkatta', 30), ('chennai', 35)]

print(sorted(tempatratures, key=lambda item: item[-1]))

''' wap to get the most repeated word '''

s = 'tu tu tu tuu meri me me me tera honelagaaa '
l = s.split()

d = {value: l.count(value) for value in l}

res = (sorted(d.items(), key=lambda item: item[-1]))
print('most repeated word', res[-1])

''' wap to print the longest word with its length '''

s = 'ha tu hai ha tu hai meri khwaboo me tuu hai'
l = s.split()

d = {word: len(word) for word in l}

res = (sorted(d.items(), key=lambda lem: lem[-1]))
print(res[-1], 'longest word in string')

''' wap to find the longest word which is not repeated '''

s = 'python is a programming language and Vidya makes programming fun !'
l = s.split()

d = {key: len(key) for key in l if l.count(key) == 1}
print(d)

res = sorted(d.items(), key=lambda item: item[-1])
print(res[-1], 'longest non repeated')


""" sort list based on names """

l = [{'name':'rama', 'class': 6, 'age': 12},
    {'name':'shyama', 'class': 12, 'age': 18},
    {'name':'bhama', 'class': 8, 'age': 13}]

# sort based on name
print(sorted(l, key=lambda item: item['name']))

# sort based on age
print(sorted(l, key=lambda item: item['age']))

# sort based on class
print(sorted(l, key=lambda item: item['class']))





'mere saaso me tu yaado me tu irado me tu hai'