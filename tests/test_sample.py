
from py_sanic_samples import __version__


print("---hello,word----")
print(__version__)
print("-----end---------")


class Variable:
    x = 1
    y = 'a'
    z = True

class TestClass:  
    def test_one(self):  
        x = "this"  
        assert 'h' in x  
  
    def test_two(self):  
        variable = Variable  
        assert hasattr(variable, 'x')

    def test_version(self):
        print("---helloword----")
        assert __version__ == '0.1.0'