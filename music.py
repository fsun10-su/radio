import os
# import random
import shutil
import json
# import try1
import try2



class Music(object):
    def __init__(self, start_path, new_file):
        self.spath = start_path
        self.new_file = new_file
        # self.son_file = son_file

    def readfile(self):
        print(os.listdir(self.spath))

    def createfile(self):
        os.makedirs(self.new_file)
    # def createsecfile(self):
    #     print(self.new_file)
    #     for time in range(6, 25):
    #         os.makedirs(f'{self.new_file}\{time}:00')


def subfile(new_file_path):
    for time in range(6, 24):
        os.makedirs(f'{new_file_path}/{time}-{time + 1}')


# def rand(path):
#     file_list = os.listdir(path)
#     maxran = len(file_list) - 1
#     ran_result = try1.random(maxran)
#     # rand_num = random.randint(0, len(file_list) - 1)
#     file_name = file_list[ran_result]
#     return os.path.join(path, file_name)

# def rand(path,filename):
#     file_list = os.listdir(path)
#     content = json.load(open(filename))
#     if path not in content.keys():
#         content[path] = range(0, len(file_list)-1)
#     maxran = len(file_list) - 1
#     while True:
#         if content[path] != []:
#             ran_result = try1.random(maxran)
#             # rand_num = random.randint(0, len(file_list) - 1)
#             content[path].remove(ran_result)
#             file_name = file_list[ran_result]
#             return os.path.join(path, file_name)
#         else:
#             pass



# def music_subfile_path(father_path,subfile_name):
#     # father_path = '/Users/sunfandi/Desktop/SU/'
#     music_subfile = os.path.join(father_path, subfile_name)
#     return music_subfile


# def rand_file():
#     order_list = [['ECS102', 'IST101', 'IST359', 'IST263', 'IST343'],
#                   ['IST343', 'IST101', 'ECS102', 'IST359', 'IST263']]
#     return order_list[random.randint(0, len(order_list) - 1)]


def music_main(father_path, new_file_path, new_file_name, order_list):
    with open('record.json','w+') as jf:
        pass
    new_file_path = os.path.join(new_file_path, new_file_name)
    music = Music(father_path, new_file_path)

    # os.remove(new_file_path)

    music.createfile()
    # 创建新父类文件夹

    subfile(new_file_path)
    # 生成子类文件夹

    music.readfile()

    inside_new_file_list = os.listdir(new_file_path)
    print(inside_new_file_list)

    # 随机抽取文件部分
    order = order_list

    with open('music_list.txt','w+',encoding='utf-8') as wf:

        for file in inside_new_file_list:
            inside_new_file = os.path.join(new_file_path, file)

            while True:
                if len(os.listdir(inside_new_file)) != 13:
                    for i in order:
                        target_file = os.path.join(father_path, i)

                        if len(os.listdir(inside_new_file)) == 13:
                            break
                        else:
                            while True:
                                file_select_result = try2.rand(target_file,'record1.json')
                                source = os.path.join(target_file,file_select_result)
                                if not source.endswith('.DS_Store'):
                                    if os.path.isfile(source):
                                        if i not in os.listdir(inside_new_file):
                                            wf.writelines(inside_new_file + ':   ' + source + '\n')
                                            shutil.copy(source, inside_new_file)
                                            inside_new_file_path = os.path.join(inside_new_file,file_select_result)
                                            new_file_name = str(len(os.listdir(inside_new_file))) + '.' + file_select_result
                                            inside_new_name_file_path = os.path.join(inside_new_file,new_file_name)
                                            os.renames(inside_new_file_path,inside_new_name_file_path)
                                            break
                else:
                    break

# 随机部分结束



    hourly_dict = {}
    for i in inside_new_file_list:
        hourly_dict[i] = os.listdir(os.path.join(new_file_path, file))
    with open('hourly_file.json', 'w', encoding='utf-8') as f:
        f.writelines(json.dumps(hourly_dict))

if __name__ == '__main__':
    new_file_name = 'adf'
    new_file_path = '/Users/sunfandi/Desktop'
    father_path = '/Users/sunfandi/Desktop/曲库/'
    order = ['男老','女青','男青']
    music_main(father_path,new_file_path,new_file_name, order)



