
import collections
from typing import Dict, NamedTuple, Optional
import numpy as np
import logging 


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


map_dict = collections.OrderedDict()

labels = ['aa', 'bb', 'cc', 'dd', 'ee']
f1_list = [0.88, 0,93, 0.87, 0.98, 0.66]
f1_macro = 0.99

logging.info(f"f1_list: {f1_list} , f1_macro: {f1_macro}")

map_dict["f1"] = [f1_list, f1_macro]

# OrderedDict([('f1', [[0.88, 0, 93, 0.87, 0.98, 0.66], 0.99])])
print(map_dict)

meature_metrics_list = []
for score_key, score_value_list in map_dict.items():
    temp_distribution = []
    for label, value in zip(labels, score_value_list[0]) :
        temp_item = {}
        temp_item["label"] = str(label)
        temp_item["value"] = value
        temp_distribution.append(temp_item)
    
    temp_dict = {}
    temp_dict["key"] = score_key
    temp_dict["value"] = score_value_list[1]
    temp_dict["distribution"] = temp_distribution

    meature_metrics_list.append(temp_dict)


print(meature_metrics_list)  

class PredictionOutput(NamedTuple):
    metrics: Optional[Dict[str, float]]
    qps: Optional[float]


def get_result()->PredictionOutput:
    metrics =  {
        'accuracy' : 0.88,
        'precision': 0.88435435,
        'recall': 0.98,
        'f1Score': 0.11
    }
    return PredictionOutput(metrics, 0.11)

reuslt:PredictionOutput = get_result()
print(reuslt.metrics)

for key, value in reuslt.metrics.items():
    meature_metrics_list.append({
        'key': key,
        'value': round(float(value), 4)
    })

print(meature_metrics_list)



metrics = {
    'accuracy' : 0.77,
    'precision': 0.68543534543,
    'recall': 0.66,
    'f1Score': 0.68
}

output = PredictionOutput(metrics, 0.99)

logging.info(f"指标: {output.metrics}")




for key, value in output.metrics.items():
    meature_metrics_list.append({
        'key': key,
        'value': float(value)
    })

print(meature_metrics_list)

metrics_list = []
for key, value in output.metrics.items():

    if key == 'precision':
        metrics_list.append({
            'key': '精确率',
            'value': round(float(value), 4),
            'description': '精确率(Precision)，查准率，表示正确预测为正的占全部预测为正的比例。'
        })
    elif key == 'recall':
        metrics_list.append({
            'key': '召回率',
            'value': round(float(value), 4),
            'description':'召回率(Recall)，查全率，表示正确预测为正的占全部实际为正的比例。'
        })
    elif key == 'f1Score':
        metrics_list.append({
            'key': 'F1值',
            'value': round(float(value), 4),
            'description': 'F1值为精确率和召回率的调和平均数，值越大越好。'
        })

logging.info(metrics_list)


