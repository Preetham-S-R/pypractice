# wap to print the keys in a dictionary

# d = {'a': 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}

# traversing through dictionary

# for keys in d:
#     print(keys, end="  ")
# print()
#
# # d.keys()
#
# for key in d.keys():
#     print(key, end="  ")
# print()
#
# # d.items()
#
# for key1, values in d.items():
#     print(key1, end="  ")

# wap to print only the values from the dictionary

# d = {'a': 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
#
# # d.values()
#
# for i in d.values():
#     print(i, end="  ")
# print()
#
# # d[key]
#
# for keys in d:
#     print(d[keys], end="  ")
# print()
#
# # d.get()
#
# for key1 in d:
#     print(d.get(key1), end="  ")
# print()
#
# # d.items()
#
# for key, value in d.items():
#     print(value, end="  ")

# wap to print the items in a dictionary along with the indices

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#
# for item in enumerate(d):
#     print(item, end= "  ")
# print()
#
# # d.items
#
# for items in enumerate(d.items()):
#     print(items, end="  ")
# print()
#
# # deep unpacking
#
# for item1, (key, value) in enumerate(d.items()):
#     print(item1, key, value, end="  ",sep=" - ")
#
# wap to create a dictionary with the character and its count pair in a string

# s = "preetham"
#
# d = {}

# for char in s:
#     d[char] = s.count(char)
# print(d)

# converting to set to reduce processing time

# for ch in set(s):
#     d[ch] = s.count(ch)
# print(d)

# without using inbuilt
# using nested for

# for i in set(s):
#     count = 0
#     for j in s:
#         if i == j:
#             count += 1
#     d[i] = count
# print(d)

# using memebership operator

# for ch in s:
#     if ch not in d:
#         d[ch] = 1
#     else:
#         d[ch] += 1
# print(d)

'''   we cant initialization and updation cannot be done simultaneously i.e
for i in s:
    d[ch] += 1
is ont possible
'''
# using default dictionary

# s = "preetham"
#
# from collections import defaultdict
#
# dd = defaultdict(int)
# print(dd)
#
# for cha in s:
#     dd[cha] += 1
# print(dd)

# wap to create a dictionary with word and its count pair
#
# s = 'preetham is awesome!, you can find preetham on instagram under the name preetham_s_r. check it out'
# d = {}
# s1 = s.split()
#
# for i in s1:
#     d[i] = s1.count(i)
# print(d)
#
# # without built in method
#
# d1 = {}
#
# for i1 in s1:
#     count = 0
#     for j1 in s1:
#         if i1 == j1:
#             count += 1
#     d1[i1] = count
# print(d1)
#
# # using membership
#
# d2 = {}
#
# for i2 in s1:
#     if i2 not in d2:
#         d2[i2] = 1
#     else:
#         d2[i2] += 1
# print(d2)
#
# # using default dictionary
#
# from collections import defaultdict
#
# d3 = defaultdict(int)
#
# for i3 in s1:
#     d3[i3] += 1
# print(d3)

# wap to create a dictionary with word and its length pair

# s = "tere mast mast do nain, mera dill ka legeye chan"
# l = s.split()
# d = {}
# for i in l:
#     d[i] = len(i)
# print(d)
#
# # wap to create a dictionary with word and its length pair only if the word is of even length
#
# s = "tere mast mast do nain, mera dill ka legeye chan"
# l1 = s.split()
# d1 = {}
#
# for i1 in l1:
#     if len(i1) % 2 == 0:
#         d1[i1] = len(i1)
# print(d1)

# wap to create a dictionary with word and its length pair only if the word is starting with vowel

# s = 'ani sutide yako indu neene ne nanaval yendu, maayada lokadinda nangagi bandaval yendu'
# l = s.split()
# d = {}
#
# for i in l:
#     if i[0] in 'aeiouAEIOU':
#         d[i] = len(i)
# print(d)

# wap to create a dictionary with word and its count only if the word is not repeated

# s = 'ani sutide yako indu neene ne nanaval yendu, maayada lokadinda nangagi bandaval yendu'
# l = s.split()
# d = {}
#
# for words in l:
#     if l.count(words) == 1:
#         d[words] = l.count(words)
# print(d)

# wap to reverse the values in the dictionary if the value is of type string

# d = {'a': 'hello', 'b': 100, 'c': 10.2, 'd': 'world'}
#
# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = value[::-1]
#
# print(d)

# wap to get all the duplicate items and the number of times the item is repeated in the list.

# l = ['apple', 'google', 'gmail', 'yahoo', 'gmail', 'apple', 'gmail', 'google']
# d = {}
#
# for i in l:
#     if l.count(i) > 1 :
#         d[i] = l.count(i)
# print(d)

# wap to get the following output

# s = 'hello world welcome to python programming hi there'
# d = {}
# l1 = s.split()
#
# for i in l1:
#     word = []
#     for j in l1:
#         if i[0] == j[0] and j not in d:
#             word += [j]
#     d[i[0]] = word
# print(d)
#
# # defaultdict
#
# from collections import defaultdict
#
# dd = defaultdict(list)
#
# for word in l1:
#     dd[word[0]] += [word]
# print(dd)

# wap to create a dictionary with element and its index pair in the given list

# l = ['apple', 'google', 'gmail', 'yahoo', 'gmail', 'apple', 'gmail', 'google']
#
# from collections import defaultdict
# d = defaultdict(list)
#
# for index, key in enumerate(l):
#     d[key] += [index]
# print(d)
#
# #
# dd = {}
# for index1, key1 in enumerate(l):
#     if key1 not in dd:
#         dd[key1] = [index1]
#     else:
#         dd[key1].append(index1)
# print(dd)

# wap to flip key and values in a dictioary

# d = {'a': 1, 'b':2, 'c': 3, 'd': 4}
# d1 = {}
# for key in d:
#     value = d[key]
#     d1[value] = key
# print(d1)
#
# d2 = {}
# for item, val in d.items():
#     d2[val] = item
# print(d2)


