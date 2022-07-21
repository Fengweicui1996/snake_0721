# -*- coding: UTF-8 -*-
# !acaconda3/bin/python
# !/usr/bin/bash


import os
import time
import config

count_limit = config.around

count_init = 1

label_path = config.path

file_name = config.serum

file_num = 'th'

while count_init <= count_limit:
    if count_init == 1:
        file_num = 'st'
    elif count_init == 2:
        file_num = 'nd'
    elif count_init == 3:
        file_num = 'rd'
    else :
        file_num = 'th'
    print(file_name + '_' + str(count_init) + file_num)
    os.system('sudo python main.py')
    time.sleep(1)
    dirs = os.listdir(label_path)
    oldName = os.path.join(label_path,file_name)
    newName = os.path.join(label_path,file_name + '_' + str(count_init) + file_num)
    os.rename(oldName,newName)
    count_init += 1
