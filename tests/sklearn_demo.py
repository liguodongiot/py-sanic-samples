import numpy as np
import logging
from sklearn.model_selection import train_test_split
import pandas as pd

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 生成数据
def create_data(data_num=100):
    # 保证在之后取随机数时都取到同一组数据
    # seed()是设置了一条世界线。细细想来甚为有趣，
    # 如：seed(10)，则表示之后取的随机数都是编号10数组中的随机数，
    # 可以理解编号10数组中有很多很多个随机数，依次向后取数。
    # 如果seed()中不填值，则会根据时间来选择某个数组。
    np.random.seed(21)
    # 正态分布，生成高斯分布的概率密度随机数
    # loc:float
    # 概率分布的均值，对应着整个分布的中心center
    # scale:float
    # 概率分布的标准差，对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高
    # size:int or tuple of ints
    # 输出的shape，默认为None，只输出一个值
    x1 = np.random.normal(1, 0.2, data_num)
    logging.info(f"x1: {x1}")
    np.random.seed(21)
    x2 = np.random.normal(2, 0.2, data_num)
    x = np.append(x1, x2)
    y = np.array([0] * data_num + [1] * data_num)
    logging.info(f"x: {x}")
    logging.info(f"y: {y}")
    return x, y


X, y = create_data(100)

df = pd.DataFrame()
df['X'] = X
df['y'] = y

print(df.sample(5))
print("-------")

# 划分训练集和测试集
train, test = train_test_split(df, test_size=0.2, stratify=df['y'])

train_label_unilist = train['y'].unique().tolist()
test_label_unilist = test['y'].unique().tolist()

all_label_unilist = df['y'].unique().tolist()


print('all:\n', df['y'].value_counts())
print('train:\n', train['y'].value_counts())
print('test:\n', test['y'].value_counts())

logging.info("end!")


