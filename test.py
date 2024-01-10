# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys
print(sys.executable)
from platform import python_version
print('py: ' + python_version())
try:
    import numpy as np
    print('np: ' + np.__version__)
except:
    print('np: not installed')
try:
    import tensorflow as tf
    print('tf: ' + tf. __version__)
except:
    print('tf: not installed')
try:
    import torch as pt
    print('pt: ' + pt. __version__)
except:
    print('pt: not installed')


if __name__ == '__main__':
    print('\nPATH:')
    [print(p) for p in sys.path]
