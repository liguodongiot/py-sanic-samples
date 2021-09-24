import math
import logging 
import os 

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 根据空行切分训练集和校验集
def get_split_dataset(input_path, output_path, valid_ratio):
    logging.info(f"开始分割文件：{input_path}")

    with open(input_path, "r", encoding='utf-8') as f:
        reader = f.readlines()

    num_item = len([item for item in reader if item=='\n'])
    total = num_item+1
    train_ratio = 1 - valid_ratio
    train_num = math.floor(total  * train_ratio)

    split_line = 0
    num_n = 0
    for i, item in enumerate(reader):
        if item == '\n':
            num_n += 1
        if num_n == train_num:
            split_line = i
            break
        
    logging.info(f"总数：{total}, 分割的训练语数：{train_num} , 分割行：{split_line}")

    train_data = reader[:split_line+1]
    dev_data = reader[split_line+1:]
    with open(output_path+'/train.txt', 'a') as f:
        f.writelines(train_data)
    with open(output_path+'/dev.txt', 'a') as f:
        f.writelines(dev_data)

# get_split_dataset("/Users/liguodong/work/data/temp/ner/one/example.dev", "/Users/liguodong/work/data/temp/ner/output", 0.2 )

def read_data_multidir(dirs: str):
    dir_list = dirs.split(',')
    logging.info(f"语料列表：{dir_list}")
    result = []
    for dir_name in dir_list:
        file_names=[os.path.join(path, name) for path, _, files in os.walk(dir_name) for name in files]
        print(f"待处理的语料文件：{file_names}")
        for file in file_names:
            get_split_dataset(file, "/Users/liguodong/work/data/temp/ner/output", 0.2)
    

# read_data_multidir("/Users/liguodong/work/data/temp/ner/two")

def copy_data_multidir(dirs: str, output_path):
    dir_list = dirs.split(',')
    logging.info(f"语料列表：{dir_list}")
    
    file_merge = open(output_path+'/test.txt', 'w')  

    for dir_name in dir_list:
        file_names=[os.path.join(path, name) for path, _, files in os.walk(dir_name) for name in files]
        print(f"待处理的语料文件：{file_names}")
        for file in file_names:
            for line in open(file): 
                file_merge.writelines(line)  
    file_merge.close() 
    
copy_data_multidir("/Users/liguodong/work/data/temp/ner/one,/Users/liguodong/work/data/temp/ner/two","/Users/liguodong/work/data/temp/ner/output")

print("over...")