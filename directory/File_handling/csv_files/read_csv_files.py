import csv
path = r"C:\Users\hp\PycharmProjects\pythonProject6\directory\File_directory\csv_files\sample.csv"
employee = r"C:\Users\hp\PycharmProjects\pythonProject6\directory\File_directory\csv_files\employees.csv"
vacination = r'C:\Users\hp\PycharmProjects\pythonProject6\directory\File_directory\csv_files\vaccination_data.csv'
shares = r'C:\Users\hp\PycharmProjects\pythonProject6\directory\File_directory\csv_files\test.csv'
from collections import defaultdict

# reader()

# with open(path) as csv_file:
#     read_obj = csv.reader(csv_file)
#     print(read_obj)
#     for row in read_obj:
#         print(row)

# DictReader()

# with open(path) as csv_file:
#     read_obj = csv.DictReader(csv_file)
#     print(read_obj)
#     for row in read_obj:
#         print(row)

''' wap to read all the names of the files in employee.csv file '''

# with open(employee) as emp:
#         read_obj = csv.reader(emp)
#         for row in read_obj:
#             print(row[0])

''' wap to print only the names with salaries greater than 70000 '''

# with open(employee) as emp:
#     r_obj = csv.reader(emp)
#     next(r_obj)          # can be used to skip one line
#     for names in r_obj:
#         sal = names[-1]
#         if int(sal) > 70000:
#             print(names[0], sal)

''' wap to group male and female employees '''

# gend = defaultdict(list)
#
# with open(employee) as emp:
#     r_obj = csv.reader(emp)
#     for gender in r_obj:
#         gend[gender[1]] += [gender[0]]
#
# print(gend)


''' wap to group employees based on their team '''

# team = defaultdict(list)
#
# with open(employee) as emp:
#     r_obj = csv.reader(emp)
#     for name in r_obj:
#         team[name[-2]] += [name[0]]
#
# print(team)

''' wap to sort the shares on test.csv file based on the share price '''

# d = defaultdict(str)
# with open(shares) as sh:
#     r_obj = csv.reader(sh)
#     next(r_obj)
#     for share in r_obj:
#         d[share[0]] += share[-1]
#     # print(d)
#     d1 = list(sorted(d.items(), key=lambda item: float(item[-1]), reverse=True))
#     print(dict(d1)
#

''' wap to add all the shares in the test.csv file '''

# with open(shares) as sha:
#     r_obj = csv.reader(sha)
#     next(r_obj)
#     total_shares = 0
#     for share in r_obj:
#         total_shares += int(share[1])
#
#     print(total_shares)

''' analyse vaccination data '''

'''total vaccination of all the countries'''

''' total vaccinations by country '''

'''names of the countries a0nd who regions '''

'''country and persons vaccinated, get top 3 countries with most vaccinated people '''

''' countries with less than 10k vaccinated people '''

''' get the latest updated country with its total vaccinations and number of people vaccinated '''

d = defaultdict(list)
with open(vacination) as file:
    r_obj = csv.DictReader(file)
    header = next(r_obj)
    for row in r_obj:
        d[row['DATE_UPDATED']] += [(row['COUNTRY'], row['TOTAL_VACCINATIONS'])]
    print(d)
res = sorted(d.items())
print(res[-1])