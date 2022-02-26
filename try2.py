# import try1
# import json
# import os
#
#
# filename = 'record.json'
# # new_dict = {}
# # with open(filename,'w') as load_f:
# #     json.dump(new_dict,load_f)
#
#
#
# path = '/Users/sunfandi/Desktop/SU/IST263/'
#
# def rand(path,filename):
#     with open(filename, 'r') as load_f:
#         content = json.load(load_f)
#     load_f.close()
#     file_list = os.listdir(path)
#     if path not in content.keys():
#         content[path] = list(range(0, len(file_list)-1))
#
#     maxran = len(file_list) - 2
#     while True:
#         if len(content[path]) >5:
#             ran_result = try1.random(maxran)
#             # rand_num = random.randint(0, len(file_list) - 1)
#             if ran_result in content[path]:
#                 print(ran_result)
#                 content[path].remove(ran_result)
#                 file_name = file_list[ran_result]
#                 print(content)
#                 with open(filename,'w') as dump_f:
#                     json.dump(content, dump_f)
#                 return os.path.join(path, file_name)
#             else:
#                 pass
#         else:
#             content[path] = list(range(0, len(file_list) - 1))
#
#
# for i in range(10):
#     rand(path, filename)
# print(rand(path, filename))



import json
import os
import random


# filename = 'record1.json'
# new_dict = {}
# with open(filename,'w') as load_f:
#     json.dump(new_dict,load_f)



# path = '/Users/sunfandi/Desktop/SU/IST263/'

def rand(path,filename):
    with open(filename, 'r') as load_f:
        content = json.load(load_f)
    load_f.close()
    file_list = os.listdir(path)
    if path not in content.keys():
        content[path] = file_list

    # maxran = len(file_list) - 2
    while True:
        if content[path] != []:
            ran_result = random.choice(content[path])
            # rand_num = random.randint(0, len(file_list) - 1)
            if ran_result in content[path]:
                # print(ran_result)
                content[path].remove(ran_result)
                # print(content)
                with open(filename,'w') as dump_f:
                    json.dump(content, dump_f)
                return ran_result
            else:
                pass
        else:
            content[path] = file_list


# for i in range(10):
#      rand(path, filename)
# print(rand(path, filename))