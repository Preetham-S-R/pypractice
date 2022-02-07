# wap to create a dictionary with item and its index pair

# s = 'hello'
# d = {}
#
# for ite,ind in enumerate(s):
#     d[ite] = ind
# print(d)
#
# # comprehension
#
# dict_ = {index: item for index, item in enumerate(s)}
# print(dict_)

# wap to create a dictionary with word and its length pair

# s = 'tu jo mila to sab kuch hai hasil'
# s1 = s.split()
# d = {}
#
# for i in s1:
#     d[i] = len(i)
# print(d)
#
# # comprehension
#
# dict_ = {word: len(word) for word in s1}
# print(dict_)

# wap to create a dictionary with char and its count pair

# s = 'tuj me rab dikh ta hai , yara mai kya karu'
# d = {}
#
# for i in s:
#     d[i] = s.count(i)
# print(d)
#
# # comprehension
#
# d1 = {item: s.count(item) for item in s}
# print(d1)

# wap to create a dictionary of word and its count

# s = 'hey ya i wanna get closer to you, hey ya i need to be closer to you'
# s1 = s.split()
#
# d = {}
#
# for i in s1:
#     d[i] = s.count(i)
# print(d)
#
# # comprehension
#
# dict_ = {item: s.count(item) for item in s1}
# print(dict_)

# wap to create a dict of word and its count pair only if the word is of even length

# s = 'hey ya i wanna get closer to you, hey ya i need to be closer to you'
# s1 = s.split()
# d = {}
#
# for i in s1:
#     if len(i) % 2 == 0:
#         d[i] = s.count(i)
# print(d)
#
# # comprehension
#
# d1 = {word: s.count(word) for word in s1 if len(word) % 2 == 0}
# print(d1)

# wap to create a dict with index and word pair if the word is of odd length reverse it else keep it as it is

# s = 'hey ya i wanna get closer to you, hey ya i need to be closer to you'
# s1 = s.split()
#
# d = {index: word if len(word) % 2 == 0 else word[::-1] for index, word in enumerate(s1)}
# print(d)

# wap to create a dict with word and its length pair only if the word is starting with vowels

# s = 'hey ya i wanna get closer to you, hey ya i need to be closer to you '
# s1 = s.split()
#
# d = {word: len(word) for word in s1 if word[0] in 'aeiouAEIOU' }
# print(d)

# wap to create a dict of item and its index pair if the item is of string data type reverse it

# l = ['a','b',1,12,5,True,'vidya']
#
# d = {index: item[::-1] if isinstance(item, str) else item for index, item in enumerate(l)}
# print(d)

# wap to create a dict of item and its index pair if the item is of string data type keep it as it is else reverse it

# l = ['java','python', 28, 2.5, True, 4+0j]
#
# d = {index: str(item)[::-1] if not isinstance(item, str) else item for index, item in enumerate(l)}
# print(d)

# wap to create a dictionary comprehension to flip or swap keys and values in a dictionary

# d = {'a': 1, 'b': 2, 'c': 3}
#
# d1 = {value: key for key, value in d.items()}
# print(d1)

# to create character and ascii value pair

# s = 'hey ya i wanna get closer to you, hey ya i need to be closer to you'
#
# d = {i: ord(i) for i in s}
# print(d)

# wap to
