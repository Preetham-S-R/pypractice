# # 1. wap to traverse through list
#
# l = ['python','java',1,2,3]
#
# for item in l:
#     print(item,end="  ")
#
# print()
#
# for i in range(len(l)):
#     print(l[i],end="  ")

# 2. wap to print index and its corresponding elements

# l = ['python','java','bava','lava',12,1.0,0.0]
#
# for ele in range(len(l)):
#     print(ele, l[ele],sep=" --> ")
# for i in range(len(l)):
#     print(i, l[i])

# for ele1, ele2 in enumerate(l):
#     print(ele1, ele2, sep=">>>>")

# 3. wap to print elements in the list in reversed order

#l = ['p2','2','me2','sh2','li2','34567', 'si2','pu2','a2','ci2','fa2']
#
# for i in reversed(l):
#    print(i, end="  ")
#
# print()
# for i1 in range(len(l)-1,-1,-1):
#     print(l[i1], end="  ")
#
# print()
# for i2 in reversed(l):
#     print(i2, end="  ")

# 4. wap to print alternate elements in a list

#l = ['p2',2,'me2','sh2','li2','ki2', 'si2','pu2','a2','ci2','fa2','piku','kiku','beku']
# #
# # using slicing
#
# for i in l[0::2]:
#     print(i, end="  ")
# print()
#
# for i1 in l[1::2]:
#     print(i1,end="  ")
# print()
#
# # using range
#
# for i2 in range(0,len(l),2):
#     print(l[i2], end='  ')
# print()
#
# for i3 in range(1, len(l), 2):
#     print(l[i3], end="  ")

# using condition

# for i4 in range(len(l)):
#     if i4 % 2 == 0:
#         print(i4, end="  ")
# print()
#
# for i5 in range(len(l)):
#     if i5 % 2 != 0:
#         print(i5, end="  ")

# 5. wap to print only integers present in a list

# l = ['p2',2,'me2','sh2','li2','ki2', 'si2','pu2','a2','ci2','fa2','piku','kiku','beku',-1,2,3,4,-5,555,4.0,45.0,0j, 1+5j, 24+15j, True, False, 2.5]
#
# for i in l:
#     if isinstance(i, int):
#         print(i, end="  ")
# print()
#
# for i2 in l:
#     if isinstance(i2, (int, complex, float, bool)):
#         print(i2, end="  ")

# 6. wap to print length of each string in the list


# l = ['p2', 'me2', 'sh2', 'li2', 'ki2', 'si2', 'pu2', 'a2', 'ci2', 'fa2', 'piku', 'kiku', 'beku']
#
# for i in l:
#     if isinstance(i,str):
#         print({i: len(i)}, sep=" > ")

# 7. wap to print the strings which are of even length

# l = ['p2',2,'me2','sh2','li2','ki2', 'si2','pu2','a2','ci2','fa2','piku','kiku','beku',1,2,3,4,5,555,4.0,45.0,0j, 1+5j, 24+15j, True, False, 2.5]
# #
# for i in l:
#     if isinstance(i, str) and len(i) % 2 == 0:
#         print(i, end="  ")
# print()
#
# l1 = []
# for i in l:
#     if isinstance(i, str) and len(i) % 2 == 0:
#         l1 += [i]
# print(l1)

# 8. wap to print the elements in the list if the element is of even length print as it is
# if element length is odd print in reverse
#
# l = ['p2',2,'me2','sh2','li2','ki2', 'si2','pu2','a2','ci2','fa2','piku','kiku','beku',1,2,3,4,5,555,4.0,45.0,0j, 1+5j, 24+15j, True, False, 2.5]
#
# even_d = []
# odd_d = []
#
# for i in l:
#     if isinstance(i, str):
#         if len(i) % 2 == 0 :
#             even_d += [i, len(i)]
#         else:
#             odd_d += [i[::-1], len(i)]
#
# print(even_d,end= "  ")
# print()
# print(odd_d)

# 9. wap to reverse the elements in the list if elements is of type string ,else keep it as it is

# l = ['p2',2,'me2','sh2','li2','ki2', 'si2','pu2','a2','ci2','fa2','piku','kiku','beku',1,2,3,4,5,555,4.0,45.0,0j, 1+5j, 24+15j, True, False, 2.5]
# #
# l1_str = []
# l2_rest = []
#
# for i in l:
#     if isinstance(i, str):
#         l1_str.append(i[::-1])
#     else:
#         l2_rest.append(i))
#
# print('reversed string in list --->', l1_str)
# print('rest of the elements in list --> ',l2_rest)

# 10. wap to print the elements which are starting with vowels

# l = ['amazon','flipkart','walmart','gmail','yahoo']
#
# for i in l:
#     if i[0] in 'aeiouAEIOU':
#         print(i)

# 11. wap to print all the extensions in the following list

# ext = ['youtube.txt','amazon.pdf','apple.xls','flipkart.in']
#
# for i in ext :
#     l,b = i.split('.')
#     print(b, end="   ")
# #
# 12. wap to print the file name if the file name is of odd length

# ext = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipkart.in']
#
# for i in ext:
#     a,b = i.split('.')
#
#     if len(a) % 2 != 0:
#         print(a)

# for item in ext:
#     a = item.split('.')
#     if len(a[0]) % 2 == 0:
#         pass
#     else:
#         print(a[0])

# 13. wap to return first occurance index of given element

# numb = [10,40,20,80,20,40,30]
# num = 40
#
# for ele in numb:
#     if ele == num:
#         print(ele, numb.index(ele), sep=" --> ")
#         break
# else:
#     print('element not present')
#
# # enumerate
#
# for index, item in enumerate(numb):
#     if item == num:
#         print(item, index, sep="  > ")
#         break

# 14. wap to check prime number

# n = 7
#
# for i in range(2, n):
#     if n % i == 0:
#         print('not prime')
#         break
# else:
#     print(n, "it's a prime")

# 15. wap to check a series of prime numbers

# n = int(input('enter a range  : '))
#
# prime = []
# for i in range(1,n):
#     if n > 1:
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             prime += [i]
# print('prime numbers in range of', n, 'is', prime)

# 16. wap to print all the elements other than the given element

# numb = [10,20,30,40,50,60,70,80,90,100]
# n = 20
#
# for i in numb:
#     if i == n:
#         continue
#     print(i, end="  ")

# 17. wap to check prime numbers in agiven list

# l = [1,2,3,5,7,11,10,15,14,13,19,20]
#
# for i in l:
#     if i > 1:
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             print(i,end="  ")

# 18. wap to print the palindromes given in the list

# l = ['python', 'dad', 'hai', 'malayalam', 'madam', 'mom']
#
# for i in l:
#     if i == i[::-1]:
#         print(i)

# 19. wap to rotate items of the list
# items = ['apple', 1.2, 'google', '12.6',26,'100']
# k = 2
# item = []
#
# for i in range(k):
#     *n, n1 = items
#     item = n1, *n
#     items = item
# print(item)
# #
# for i in items:
#     *n, n = items
#     item = n, *n
#     items = item
# print(item)


# # from collections import deque
# i = ['apple', 1.2, 'google', '12.6',26,'100']
# l = deque(i)
# l.rotate(2)
# print(list(l))

# print sum of entire list and sum of only internals
# l = [[1,2,3],[4,5,6],[7,8,9]]
# #
# sum_int = 0
# sum_total = 0
#
# for i in l:
#     sum_int = 0
#     for j in range(len(i)):
#         sum_int = sum_int + i[j]
#     print(sum_int)
#     sum_total += sum_int
# print(sum_total)

#

# for item in l:
#     sum_int = 0
#     for i in item:
#         sum_total += i
#         sum_int += i
#     print(sum_int)
# print(sum_total)

# rotate list based on k value

# l = ['apple',1.2,'google','12.6',26,'100']
# k = 2
# for i in range(k):
#     item = l.pop()
#     l = [item] + l
#     # l.insert(0, item)
# print(l)
