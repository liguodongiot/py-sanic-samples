import json
import re
import pandas as pd
import math
import logging 
import os

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

def read_data_single(data_path: str):
    '''
    数据读取
    '''
    with open(data_path, "r", encoding='utf-8') as f:
        reader = f.readlines()
        lines = []
        for line in reader:
            line_dict = json.loads(line.strip())
            line_dict['labels'] = line_dict['labels'][0]
            lines.append([line_dict['text'], line_dict['labels']])
 
    return lines




def read_data_multidir(dirs: str):
    dir_list = dirs.split(',')
    logging.info(f"语料列表：{dir_list}")
    result = []
    for dir_name in dir_list:
        file_names=[os.path.join(path, name) for path, _, files in os.walk(dir_name) for name in files]
        print(f"待处理的语料文件：{file_names}")
        for file in file_names:
            result.extend(read_data_single(file))
            
    df = pd.DataFrame(result, columns=['sentence', 'label'])
    df['sentence'] = df['sentence'].map(lambda x: re.sub('\s', '', x))
    return df

df = read_data_multidir("/Users/liguodong/work/data/temp/classify/one,/Users/liguodong/work/data/temp/classify/two")


print(df.shape)
print(df.sample(5))
