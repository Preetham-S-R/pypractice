# #wap to check if the user input number is even or not.
#
# # a = int(input("enter a number :  "))
# a = 5
# if a % 2 == 0:
#     print("the given number is even")
#
# else:
#     print('the given number is odd')



# wap to check if the  given character is in lower case or not

#
# c = input('enter a character to check :  ')
#
# #if 'a'<= c <= 'z':
# if c.islower() == True :
#      print('the character',c,'is a lower case character')
#
# else :
#     if c.isupper() == True :
#         print ('the character',c,'is in upper case')
#
#     else:
#         print('the character',c,'is not a alphabet')


# OR


# c = input('enter a character to check :  ')
#
#
# if c.islower() == True :
#     print('the character',c,'is a lower case character')
#
# elif c.isupper() == True :
#     print ('the character',c,'is in upper case')
#
# else:
#     print('the character',c,'is not a alphabet')




# # wap to check if the given element is present in the collection or not
#
# a = list(input('enter a collection :  '))
# e = input('enter a element to be checked :  ')
# print(a)
# if e in a :
#     print('the element',e,'is present in the collection')
# else:
#     print('the element is not present in collection')



# # wap to check if the given iterable is empty or not
#
# itera = 'hai'
#
# if len(itera) == 0 :
#     print('the iterable is empty')
# else :
#     print('the iterable is not empty')

# OR


# itera = 'hai'
#
# if bool(itera):
#     print('the iterable is not empty')
# else :
#     print('the iterable is empty')

# OR


# itera = 'hai'
#
# if itera :
#     print('iter is not empty')
# else :
#     print('iterable is empty')

# wap to check if the given value is default or non default value

# a = 0
#
# if a :
#     print ('the vale is non default')
# else :
#     print('value is default')


# wap to convert lowercase letter into upper and upper to lower

# a = input('enter a string :  ')
# #
# if a.isalpha():
#     print(a.swapcase())
# else:
#     print('the string is not a alphabet')



# OR
#
# if a.islower():
#     print(a.upper())
# elif a.isupper():
#     print(a.lower())
# else:
#     print('not a alphabet')

# OR


# chr(ord('a')-32)
#
# chr(ord('A')+32)

# wap to check is the string is starting with vowels or not

# i = input('enter a string :  ')
#
# if i[0] in 'aeiouAEIOU' :
#     print('the string starts with vowel')
# else:
#     print('the sting does not start with vowel')
#

# wap to check if the given string is ending with vovel or not

# a2 = input('enter a string:  ')
#
# if a2[-1] in 'aeiouAEIOU':
#     print('vovel present at end')
# else:
#     print('vowel not present art end')



# # check if the string is palindrome or not
#
# a = input('enter a string :  ')
# a = a.lower()
#
# if a == a[::-1]:
#     print('string is a palindrome')
# else:
#     print('string is not a palindrome')


# wap to check if integer is a palindrome or not

# a= int(input('enter a number :  ')
# b = str(a)
#
# if b == b[::-1]:
#     print('is palindrome')
# else:
#     print('not palindrome')



# wap to check if the iterable has even number of elements

# a = input('enter a string:  ')
#
# if len(a)%2 == 0:
#     print('even')
# else:
#     print('odd')


# WAP to check if the first digit in the given number is even or odd

# n = int(input('enter a number:  '))
# b = str(n)
#
# if int(b[0]) % 2 == 0:
#     print('even')
# else:
#     print('odd')


# # wap to check greatest of 3 numbers
#
# n1 = int(input('enter 1st number:  '))
# n2 = int(input('enter 1st number:  '))
# n3 = int(input('enter 1st number:  '))
#
# if n1>n2 and n1>n3:
#     print(n1, 'is the greatest no')
# elif n2>n3:
#     print(n2, 'is the greatest no')
# else:
#     print(n3, 'is the greatest no')
#

# wap to check if the eneterd character is vowel or not. if it is a vowel create a dictionary with char
# as key and ascii as value

# char = input('enter a character:  ')
# a = []
# if len(char)==1:
#     if char in 'aeiouAEIOU':
#         a+=[char]
#         print(dict.fromkeys(a,ord(char)))
#     else:
#         print('the character is not a vowel')

# OR

# char = input('enter a character:  ')
# d = {}
#
# if char in 'aeiouAEIOU':
#     #d[char]=ord(char)
#     #d.update({char:ord(char)})
#     d.setdefault(char,ord(char))
#     print(d)
# else:
#     print('the character is not a vowel')


