# 1. wap to traverse through set and print each element

# set_ = {'python', 'dad', 'hai', 'malyalam', 'madam'}
#
# for item in set_:
#     print(item, end="  ")

# 2. wap to print the elements in the set in reversed order

# set_ = {'python', 'dad', 'hai', 'malyalam', 'madam'}
# not possible

# 3. wap to remove the given element from the set

set_ = {'python', 'dad', 'hai', 'malyalam', 'madam'}
# set_.discard('dfhjkh')
remove = 'python'
# # print(set_)
# # set_.discard(remove)
#print(set_)
#
# """ set after making changes to it's elements will reshuffel and this will lead to an error in traversing(real time error)"""

# for item in set_:
#     set_.discard(remove)
#     break
# print(set_)
#
# wap to creat a set with list elements if the elenment is palindrome

# list_ = ['python', 'dad', 'hai', 'malayalam', 'madam','mom']
# set_ = set()
#
# for i in list_:
#     if i == i[::-1]:
#         set_.add(i)
# print(set_)

# enumerate on set

# set_ = {'python', 'dad', 'hai', 'malyalam', 'madam'}
#
# print(list(enumerate(set_)))

# wap to create a setwith all the languages starting with 'p'

# lang = {'python','java','perl','PHP','python','js','c++','js','python','ruby'}
# set_ = set()
#
# for i in lang:
#     if i[0] in 'Pp':
#         set_.add(i)
# print(set_)

#wap to remove all duplicates in the list

l = ['apple','google','apple','yahoo','google']

# count
res = []
for item in l:
    # if l.count(item) == 1:
    if item not in res:
       res.append(item)

print(res)

#