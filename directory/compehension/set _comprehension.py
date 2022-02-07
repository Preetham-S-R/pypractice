# to create a set of squares from 1 to 10

# s = {i**2 for i in range(1,11)}
# print(s)

# wa set comprehension to create a set of tuples of index and item

# s = {i for i in enumerate(range(11))}
# print(s)
#
# l = ['uff', 'teri','aada']
#
# s1 = {(item,l[item]) for item in range(len(l))}
# print(s1)

# wa se t comprehension to create set of tuples with item and its length pair

l = ['uff', 'teri', 'aada', 'i', 'like', 'the', 'way', 'you', 'move']

s = {(item, len(item)) for item in l}
print(s)
