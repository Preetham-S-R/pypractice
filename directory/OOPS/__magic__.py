class Dad:
    l_name = 'Iyer'

    def __init__(self, m):
        self.m = m

    def get_name(self):
        print(self.m, self.__class__.l_name)


class Mom(Dad):

    def __init__(self, mn, m):
        self.mn = mn
        super(Mom, self).__init__(m)

    def get_name(self):
        print(self.mn, self.m, self.__class__.l_name)


class Child(Dad):

    def __init__(self, c, m):
        self.c = c
        super(Child, self).__init__(m)

    def get_name(self):
        print(self.c, end=" ")
        super(Child, self).get_name()


a = Child('Chinnaswmy', 'Mutthuswamy')
b = Dad('Mutthuswamy')
c = Mom('sunita', 'Muttuswamy')
a.get_name()
b.get_name()
c.get_name()

#
# import time
#
#
# class Delay:
#     def __init__(self, func):
#         self.func = func
#         self.delay = 10
#
#     def __call__(self, *args, **kwargs):
#         time.sleep(self.delay)
#         a = self.func(*args, **kwargs)
#         return a
#
# @Delay
# class Addititon:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#
# b = Addititon(1, 2)
#
# print(b.add())



# i/p = 'aaabbbddeecccc'    o/p = '3a3b2d2e4c' "a3b3d2"

# a = '@aaabbbddee@@@__cccc'
# l = ''
#
#
# for i in a:
#     if i not in l:
#         count = 0
#         for j in range(len(a)):
#             if a[j] == i:
#                 count += 1
#         else:
#             l += i
#             l += str(count)
# #
# print(l)




#

# s = ''
# l = []
#
# for i in a:
#     c = 0
#     if i not in l:
#         l.append(i)
#         for j in a:
#             if i == j:
#                 c += 1
#             else:
#                 break
#         s = s + str(c) + i
#
# print(s)


##


# s = 'aabbbccccaaa'
# # i = 0
# count = 0
# res = ''
# while i < len(s):
#     if s[i] == s[i+1 : i+2]:
#         count += 1
#         i += 1
#     else:
#         count += 1
#         res += s[i] + str(count)
#         count = count - count
#         i += 1
# print(res)

# for i in range(len(s)):
#     if s[i] == s[i+1:i+2]:
#         count += 1
#     else:
#         count += 1
#         res += s[i] + str(count)
#         count = count - count
# print(res)



# for i in a:
#     if i not in l:
#         count = 0
#         for j in range(len(a)):
#             if a[j] == i:
#                 count += 1
#         else:
#             l += i
#             l += str(count)
# #