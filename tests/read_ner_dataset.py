
from typing import List
from typing import Tuple

def read_conll_format_file(file_path: str,
                               text_index: int = 0,
                               label_index: int = 1) -> Tuple[List[List[str]], List[List[str]]]:
        """
        Read conll format data_file
        Args:
            file_path: path of target file
            text_index: index of text data, default 0
            label_index: index of label data, default 1
        Returns:
        """
        x_data, y_data = [], []
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
            x: List[str] = []
            y: List[str] = []
            for line in lines:
                rows = line.split(' ')
                if len(rows) == 1:
                    x_data.append(x)
                    y_data.append(y)
                    x = []
                    y = []
                else:
                    x.append(rows[text_index])
                    y.append(rows[label_index])
        return x_data, y_data

x_data, y_data = read_conll_format_file('/Users/liguodong/work/data/china-people-daily-ner-corpus/example.dev')

result = sum(y_data, [])
result = list(set(result))
# ['O', 'I-LOC', 'I-ORG', 'B-LOC', 'B-PER', 'I-PER', 'B-ORG']
print(result)




