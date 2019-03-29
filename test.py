# -*- coding: utf-8 -*-

#   2019/3/28 0028 上午 8:48     

__author__ = 'RollingBear'

file_name = input('please input file name:')

with open(file_name, 'r') as f:
    name_list = []
    result = f.readlines()
    print(result)
    for count in range(len(result)):
        result[count] = result[count].replace('\n', '')
        result_flag = result[count].split(' ')
        result_flag[1] = int(result_flag[1])
        name_list.append(result_flag)

name_list = sorted(name_list)

print(name_list)
for count in range(len(name_list)):
    print(name_list[count])