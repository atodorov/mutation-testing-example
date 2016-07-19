#import os
#import sys
#import importlib

#path = os.path.dirname(__file__)
#path = os.path.join(path, "ham")
#if not path in sys.path:
#    sys.path.append(path)

#module = importlib.import_module('sandwich.ham.ham')
#ham_class = module.__dict__[module.__all__[0]]

from sandwich.ham import ham
ham_class = ham.Ham


