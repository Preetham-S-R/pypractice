# wap to create a list( of tuples which is having index and its corresponing item

# l = [1,2,3,4,5,6]
# l_index = []
# # normal method
#
# for item in enumerate(l):
#     l_index.append(item)
# print(l_index)
#
# # comprehension
#
# l2 = [i for i in enumerate(l)]
# print(l2)

# wap to create a list of even numbers from the below list

# l = list(range(11))
# l1 = []
# for i in l:
#     if i % 2 == 0:
#         l1 += [i]
# print(l1)
#
# # comprehension
#
# l2 = [item for item in l if item % 2 == 0]
# print(l2)

# create 2 lists of even and odd numbers

# l = list(range(11))
#
# even = []
# odd = []
#
# for i in l:
#     if i % 2 == 0:
#         even += [i]
#     else:
#         odd += [i]
# print(even, odd)

# comprehension

# l = list(range(11))
#
# even1 = [i for i in l if i % 2 == 0]
# odd1 = [o for o in l if o % 2 != 0]
# print(even1, odd1)

# wap to create a list using the following list if the word is of even length store the word as it is , if it is
# of odd length reverse and store it

# l = ['aasdas','asdas','asfxc','asd']
#
# evens = []
# odds = []
#
# for item in l:
#     if len(item) % 2 == 0:
#         evens.append(item)
#     else:
#         odds.append(item[::-1])
# print(evens, odds)

# comprehension

# l = ['aasdas','asdas','asfxc','asd']
#
# res = [item if len(item) % 2 == 0 else item[::-1] for item in l]
# print(res)

# wap to create a list from the following list if the elements are of type string keep them as it is else reverse it

# l = ['java','python', 10 , True, 1.4, 'c++', 'ruby']
# l1 = []
# for i in l:
#     if isinstance(i, str):
#         l1.append(i)
#     else:
#          l1.append(str(i)[::-1])
# print(l1)
#
# # comprehension
#
# l2 = [item if isinstance(item, str) else str(item)[::-1] for item in l]
# print(l2)

#  write a list comprehension to create a list with a strings starting with vowels

# l = ['apple', 'eat', 'day', 'every','says', 'doctor']
#
# l2 = [i for i in l if i[0] in 'aeiouAEIOU']
# print(l2)

# wap

l = [i if i % j == 0 else None for i in range(2, 50) for j in range(2, i)]
print(l)
