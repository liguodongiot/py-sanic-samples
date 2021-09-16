import json
import re
import pandas as pd
import math
import logging 


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
    df = pd.DataFrame(lines, columns=['sentence', 'label'])
    df['sentence'] = df['sentence'].map(lambda x: re.sub('\s', '', x))
    return df


df = read_data_single("/Users/liguodong/work/data/temp/classify/one/one.txt")

print(df)

print("---------------")

def read_data_milti(data_path: str):
    with open(data_path, "r", encoding='utf-8') as f:
        reader = f.readlines()
        lines = []
        for line in reader:
            line_dict = json.loads(line.strip())
            # 取出多标签label, \t分隔
            multi_label = '\t'.join(line_dict['labels'])
            lines.append([line_dict['text']] + [multi_label])
    df = pd.DataFrame(lines, columns=['sentence', 'label'])
    df['sentence'] = df['sentence'].map(lambda x: re.sub('\s', '', x))
    logging.info(f"temp data: {df[:5]}")
    return df


df2 = read_data_milti("/Users/liguodong/work/data/temp/multiclassfy/one/one.txt")

print(df2)

print("---------------")

def read_data_sim(data_path: str):
    with open(data_path, "r", encoding='utf-8') as f:
        reader = f.readlines()
        lines = []
        for line in reader:
            line_dict = json.loads(line.strip())
            line_dict['labels'] = line_dict['labels'][0]
            lines.append([line_dict['text'], line_dict['text2'], line_dict['labels']])
    df = pd.DataFrame(lines, columns=['sentence', 'sentence2', 'label'])
    df['sentence'] = df['sentence'].map(lambda x: re.sub('\s','', x))
    df['sentence2'] = df['sentence2'].map(lambda x: re.sub('\s','', x))
    return df


df3 = read_data_sim("/Users/liguodong/work/data/temp/sim/one/one.txt")

print(df3)

print("---------------")

# 根据空行切分训练集和校验集
def get_split_dataset(input_path, output_path, valid_ratio):
    with open(input_path, "r", encoding='utf-8') as f:
        reader = f.readlines()

    num_item = len([item for item in reader if item=='\n'])
    total = num_item+1
    train_ratio = 1 - valid_ratio
    train_num = math.floor(total  * train_ratio)

    logging.info(total)
    logging.info(train_num)

    split_line = 0
    num_n = 0
    for i, item in enumerate(reader):
        if item == '\n':
            num_n += 1
        if num_n == train_num:
            split_line = i
            break
        
    print(split_line)

    train_data = reader[:split_line+1]
    dev_data = reader[split_line+1:]
    with open(output_path+'/train.txt', 'w') as f:
        f.writelines(train_data)
    with open(output_path+'/dev.txt', 'w') as f:
        f.writelines(dev_data)


get_split_dataset("/Users/liguodong/work/data/temp/ner/one/example.dev", "/Users/liguodong/work/data/temp/ner/output", 0.2 )

print("end!!!")

