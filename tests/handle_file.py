import json
import re
import pandas as pd
import math
import logging 
import os

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        print(root) #当前目录路径  
        print(dirs) #当前路径下所有子目录  
        print(files) #当前路径下所有非目录子文件 
    
    print('------------')
    # 返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。
    print(os.listdir(file_dir))
    print('------------')
    # 获取每个文件的具体路径
    file_names=[os.path.join(path, name) for path, subdirs, files in os.walk(file_dir) for name in files]
    print(file_names)
    file_names2=[os.path.join(path, name) for path, subdirs, files in os.walk(file_dir) for name in files if os.path.splitext(name)[-1]=='.txt']
    print(file_names2)
    
    print('------------')
    # 只获取文件名
    filenames = [f for f in os.listdir(file_dir) if os.path.isfile(os.path.join(root, f))]
    print(filenames[:10])
    print('------------')
    # 只获取文件名
    _, _, filenames = next(os.walk(file_dir))
    print(filenames [:10])
    print("end!")


file_name('/Users/liguodong/work/data/temp/classify/one')
