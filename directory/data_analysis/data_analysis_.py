import csv

salary_data = r'C:\Users\hp\PycharmProjects\pythonProject6\directory\File_directory\csv_files\Salary Dataset.csv'

import csv
from collections import defaultdict

data_list_dict = []
company_salary = defaultdict(list)

with open(salary_data, encoding="utf8") as sal_csv:
    data = csv.DictReader(sal_csv)
    rows = next(data)
    for row in data:
        if True:
            data_list_dict.append(row)
            company_salary[row['Job Title']] += [[row['Company Name'], row['Salary']]]
# print(data)
# print(data_list_dict)
print(company_salary)