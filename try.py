import os

new_file_path = '/Users/sunfandi/Desktop/曲库/男青/'
inside_new_file_list = os.listdir(new_file_path)
for file in range(len(inside_new_file_list)):
    print(inside_new_file_list[file])
    file = str(file) + '.' + inside_new_file_list[file]
    inside_new_file = os.path.join(new_file_path, file)
    print(inside_new_file)