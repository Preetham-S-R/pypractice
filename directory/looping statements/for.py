# 1. wap to print 1 t0 10
# for num in range(1,11):
#     print(num)

# 2. wap to print -1 to -10

# for num in range(-1,-11,-1):
#     print(num)

# 3. wap to print -10 to -1

# for num in range(-10,0):
#     print(num)

# 4. wap to print even number from 1 to 10

# for num in range(1,11):
#     if num % 2 == 0:
#         print(num)

# 5. wap to traverse through string

# s = 'dinga dingi'
#
# for i in range(0, len(s)):
#     print(s[i])

# 6. wap to traverse through list

# l = [1,2,3,4,'a','abc',[10,20]]
#
# for item in l:
#     print(item, end="  ")

# 7. wap to traverse through tuple

# t = (1,2,3,4,0j,True,'hai','bye')
#
# # for item_num in t:
# #     print(item_num, end='   ')
#
# # OR
#
# for index in range(len(t)):
#     print(t[index])

# 8. wap to traverse through set

# set_ = {'hai','hello','bye',1,2,3,0j,True,'done'}
#
# for ele in set_:
#     print(ele)

# 9. wap to traverse through dictionary

# dict_ = {'hai': 1, 'hello': 2, 'p': 10, 'cat': 6, 'dog': 69}
#
# for key in dict_:
#     print(key, dict_[key], sep=" ----> ")

# 10. wap to print index and the element in a string

# s = 'howdy Preetham'
# # #
# # # for ele in range(len(s)):
# # #     print(s[ele], ele, sep=" -----> ")
# #
# # # OR
# #
# # for ele in enumerate(s):
# #     print(ele)
# #     print(ele[0],ele[1])
# # OR
# for index, item in enumerate(s):
#     print(index, item)
#
#  11. wap tot traverse through a string in reverse order

# s = 'preetham'
#
# # for item in range(len(s)-1,-1,-1):
# #     print(s[item], end='  ')
# #
# # for char in s[::-1]:
# #     print(char, end='  ' )
#
# for item in reversed(s):
#     print(item, end='  ')

# 12. wap to count char present in a string

# s = 'preetham'
# count = 0
# for _ in s:
#     count += 1
# print(count)

# 13. wap to print even indexed charcters in the string

# s = 'preetham'
#
# for char in s[::2]:
#     print(char, end='  ')

# 14. wap to print the digits present inside the string

# s = 'hello 123 hai 69'
#
# for char in s:
#     if char.isnumeric():
#         print(char, end='  ')

# # OR
# for ch in s:
#     if '0' <= ch <= '9':
#         print(ch, end='  ')

# 15. wap to count the no of digits present in the string

# s = 'ding 1231234 jfjaj123'
# count = 0
#
# for char in s:
#     if char.isnumeric():
#         count += 1
# print(count)

# 16. wap to count the no of special characters in a string

s = 'abc dAbCD12334!@#$%^&**(<>?:'

count_spl = 0
count_cap = 0
count_sml = 0
count_dig = 0

for ele in s:
    if 'a' <= ele <= 'z':
        count_sml += 1
    elif 'A' <= ele <= 'Z':
        count_cap += 1
    elif '0' <= ele <= '9':
        count_dig += 1

    else:
        count_spl += 1

print('capital letters --> ',count_cap)
print('small letters --> ',count_sml)
print('numbers --> ',count_dig)
print('special characters --> ',count_spl)


