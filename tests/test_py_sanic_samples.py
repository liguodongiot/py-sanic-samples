import os
import sys

# base_dir = os.path.abspath(os.path.dirname(__file__))
# print(base_dir)

# sys.path.append(os.path.dirname("/Users/liguodong/work/github/py-sanic-samples/py_sanic_samples"))


from py_sanic_samples import __version__


def test_version():
    print("-------")
    assert __version__ == '0.1.0'

# test_version()
print("-------")

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
    
