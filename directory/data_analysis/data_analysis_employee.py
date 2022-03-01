import csv
from collections import defaultdict

path = r'C:\Users\hp\PycharmProjects\pythonProject6\directory\File_directory\csv_files\employees.csv'

# with open(path) as f:
#     rows = csv.reader(f)
#     for row in rows:
#         print(row)
#
# with open(path) as f:
#     rows = csv.DictReader(f)
#     for row in rows:
#         print(row['name'], row['pay'])


# def read_csv():
#     with open(path) as f:
#         records = []
#         rows = csv.DictReader(f)
#         for row in rows:
#             records.append(row)
#     return records
#
# print(read_csv())

"""total pay for all the employees"""


# def total_pay():
#     with open(path) as f:
#         total_salary = 0.0
#         rows = csv.DictReader(f)
#         for row in rows:
#             total_salary += int(row['pay'])
#     return total_salary
#
#
# print(total_pay())

"""count of male and female employees"""


# def gender():
#     with open(path) as f:
#         data = csv.DictReader(f)
#         d = defaultdict(int)
#         for item in data:
#             g = item['gender']
#             d[g] += 1
#     return d
#
# print(gender())

"""diff based on teams"""

with open(path) as f:
    data = csv.DictReader(f)
    teams = set([item['team'] for item in data])
    print(teams)
