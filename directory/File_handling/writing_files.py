path = r'C:\Users\hp\PycharmProjects\pythonProject6\directory\File_directory\txt_log_files'
f_path = r'C:\Users\hp\PycharmProjects\pythonProject6\directory\File_directory\txt_log_files\sample.log'


''' * ADD 2 BACKSLASHES AT THE END OF THE PATH STRING '''

''' wap to copy the content of sample.txt into different file '''


with open(f_path, 'r') as file_read, open(path+ "file1.txt", 'w') as file_write:
        for line in file_read:
            file_write.write(line)
print(file_write)
