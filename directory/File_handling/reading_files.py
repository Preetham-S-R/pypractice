path = r"C:\Users\hp\PycharmProjects\pythonProject6\directory\File_directory\txt_log_files\sample.txt"
access = r"C:\Users\hp\PycharmProjects\pythonProject6\directory\File_directory\txt_log_files\access-log.txt"
football = r"C:\Users\hp\PycharmProjects\pythonProject6\directory\File_directory\txt_log_files\football.txt"

from itertools import islice
from collections import defaultdict, Counter, deque


# with open(path) as f:
#     data = f.read()
#     print(data)
#     print(f.tell())
#     f.seek(0)
#     print(f.read(10))

# with open(path) as file:
#     print(file.readline(10))    # reads 10 characters from the first line
#     print(file.readline(5))     # reads 5 characters after the previous output
#     print(file.readline())      # reads the left out characters in the line


# with open(path) as file:
    # print(file.readlines())

''' wap to read all the lines present in the file WITHOUT LOADING ALL THE LINES IN A MEMEORY '''

# with open(path) as file:
#     for lines in file:
#         print(lines)

''' wap to count no of lines present in the file '''

# count = 1
# with open(path) as files:
#     for _ in files:
#         count += 1
# print('no of lines present is', count)

''' wap to print the line and it's number '''


# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         print(count, line)

# enumerate

# with open(path) as file:
#     for line_no, line in enumerate(file, start=1):
#         print(line_no, line)


''' wap to count the number of words in the given file'''

# with open(path) as file:
#     word = 0
#     for line in file:
#         l = line.split()
#         word += len(l)
#     print(word, 'is number of words in list')

''' wap to print the lines from the last'''

# l = []
# with open(path) as file:
#     for line in file:
#         l = [line] + l
#
# for i in l:
#     print(i)
#
#
# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line)

''' wap to count the no of spaces in the given file '''

# count = 0
# with open(path) as file:
#     for line in file:
#         count += line.count(' ')
#     print(count, ' is the no of space in the file')

''' wap to count the number of words that are starting with vowels '''

# count = 0
# with open(path) as file:
#     for lines in file:
#         l = lines.split()
#         for i in l:
#             if i[0] in 'aeiouAEIOU':
#                 count += 1
#     print(count, 'is the number of words starting with vowels')

''' wap to create a dictionary of word and it's count pair in the given pair '''

# d = {}
# with open(path) as file:
#     for line in file:
#         for word in line.split():
#             if word not in d:
#                 d[word] = 1
#             else:
#                 d[word] += 1
#     print(d)

#  METHOD 2: DEFAULT DICT


#
# dd = defaultdict(int)
#
# with open(path) as file:
#     for lines in file:
#         l = lines.split()
#         for word in set(l):
#             dd[word] += l.count(word)
#     print(dd)


''' Wap to extract all the ip adress from axcesslog.txt file '''

# l = []
# with open(access) as acs:
#     for lines in acs:
#         if lines.strip():
#             l1 = lines.split()
#             l.append(l1[0])
# print(l)

''' Wap to create a dictionary with ip adress and their count '''

# count = 0
# dd = defaultdict(int)
#
# with open(access) as acs:
#     for lines in acs:
#         if lines.strip():
#             l = lines.split()
#             dd[l[0]] += 1
# print(dict(sorted(dd.items(), key=lambda items: items[-1], reverse=True)))

# Counter method

# l = []
# with open(access) as acs:
#     for lines in acs:
#         if lines.strip():
#             l1 = lines.split()
#             l.append(l1[0])
# # print(l)
#
# ip_ = Counter(l)
# print(ip_)

''' COUNTER IS A CLASS IN COLLECTION MODULE WHICH IS USED  TO COUNT THE NO OF ELEMENTS PRESENT IN AN ITERABLE.
Counter creates a counter object which will have a dictionary of element and its count pair, to get the values 
in terms of tuple we can use most_common method present in counter class
 
* most_common method can take an argument which will be an integer , this integer suggests the number of elements 
(most common elements) to be printed '''

''' wap to print nth line in a file '''

# nth = 5
# with open(access) as acs:
#     n = int(input('enter a no : '))
#     for lines_no, line in enumerate(acs, start=1):
#         if n == lines_no:
#             print(line)
#             break

#

# n = 5
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         if n == count:
#             print(line)
#             break

''' islice '''

''' slice  a file to get nth lines '''

# n = 3
# with open(path) as files:
#     res = islice(files, n-1, n)
#     print(list(res))

''' wap to print first n lines '''

# n = 3
# with open(path) as files:
#     res = islice(files, 0, n)
#     print(list(res))

#

# with open(path) as file:
#     for line_no, line in enumerate(file):
#         if line_no < n:
#             print(line)

''' wap to print last n lines '''

# n = 3
# l = []
# with open(path) as f:
#     for line_no, line in enumerate(reversed(list(f))):
#         if line_no < n:
#             print(line)

# Method : 2

# n = 3
# with open(path) as f1:
#     l = len(list(f1))
#     print(l)
#     f1.seek(0)   # once the file has been iterated through , it has to be seeked backed to first line
#     res = islice(f1, l-n, l)
#     print(list(res))

# Method : 3

''' deque '''

# n = 3
# with open(path) as file:
#     res = deque(file, n)
#     print(list(res))


''' finding the length of each line in a text file '''

''' extracting messages from sample.log '''

''' counting number of INFO, WARN, TRACE messages '''

''' reading  country text from football.txt '''

# with open(football, encoding='UTF-8') as ball:
#     for line in ball:
#         if line.strip():
#             country = line.split('\t')
#             print(country[1])


''' least and most occurances of the word '''

# d = defaultdict(int)
# with open(path) as files:
#     for lines in files:
#         if lines.strip():
#             l = lines.split()
#             for word in l:
#                 d[word] += 1
#
# print(d)
# c = Counter(d)
# most, *rest, least = c.most_common()
# print(most, least)

''' wap to add all the shares in the test.csv file '''

with open(shares) as sha:
    r_obj = csv