''' 1  wap to get the indices of each items in list  '''

#
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# d = {}
# for index, key in enumerate(names):
#     if key not in d:
#         d[key] = [index]
#     else:
#         d[key] += [index]
# print(d)

''' 2  reverse the values in the dictionary if the value is of string type '''

# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
#
# d1 = {key: value[::-1] if isinstance(value, str) else value for key, value in d.items()}
# print(d1)


''' 3   wap to get all the duplicate items and the number of times the item is repeated in the list '''

# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
#
# d = {}
#
# for i in names:
#     if i not in d:
#         d[i] = names.count(i)
# print(d)

''' 4  create dictionary of city and population pairs using dict comprehension '''

# cities = ['tokyo', 'delhi', 'shanghai', 'sao paulo', 'mumbai']
# population = ['38,001,000', '25,703,168', '23,740,778', '21,06,245', '21,042.538']
#
# d = {}
#
# for cit, pop in zip(cities, population):
#     if cit not in d:
#         d[cit] = pop
#     else:
#         d[cit] += pop
# print(d)
#
# d1 = {cit: pop for cit, pop in zip(cities, population)}
# print(d1)

''' 5  wap to flip keys and values '''

# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
#
# d1 = {value: key for key, value in d.items()}
# print(d1)

''' 6  group even and odd index values with comprehension '''

# l = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 7, 8, 8, 8, 88, 99, 100]
#
# d_even = {'even': [items] for ind, items in enumerate(l) if ind % 2 == 0}
# print(d_even)
# d_odd = {'odd': [items] for ind, items in enumerate(l) if ind % 2 != 0}
# print(d_odd)
''' grouping of elements in dictionary comprehension is not possible '''

''' 7  group both the dictionary items in a single dictionary using comprehension '''

D = {'names': 'apple', 'ID': 152778}
d = {'names': 'apple', 'ID': 657678}
l = list(zip(D,d))
print(l)
# d1 = {key: value for key, value in zip({**d, **D})}
# print(d1)
#
# d3 = zip({**d, **D})
# print(list(d3))

''' 8  create dictionary with items in tuple as key and it's unicode as value using dict comprehension '''

# t = (9, 56, 78, 123, 456)
#
# d = {key: chr(key) for key in t}
# print(d)


''' 9  create dictionary taking keys and values using items in list, take key before special char
       and value after spl char  using dict comprehension '''

# list_ = ['food@table', 'lilly@flower', 'human@walk', 'being@work']
#
# d = {key.split('@')[0]: key.split('@')[1] for key in list_}
# print(d)

''' 10  create a dictionary with key as string item and value as integer using items in set and using comprehension '''

s = {(4, 56, 78), ('one', 'two', 'three')}
#
l1, l2 = s
# # l = l1, l2
# #
# # d = {}
# #
# # for i in range(len(l[0])):
# #     for j in range(len(l[1])):
# #         d[l[i]] = j
# #
# # print(d)
l = list(zip(l2, l1))
print(l)
d = {key: value for key, value in l}
print(d)

