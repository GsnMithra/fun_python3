import sys
import numpy as np
import matplotlib.pyplot as plt

def recaman(r):
    n = 0
    non_empty = set()
    r_list = []
    for i in range(r):
        if(n - i > 0 and (n - i) not in r_list):
            n = n - i
            non_empty.add(n)
            r_list.append(n)
            # print(n, end = ' ')
        else:
            n = n + i
            non_empty.add(n)
            r_list.append(n)
            # print(n, end = ' ')
    plt.plot(r_list)
    plt.show()

try:
    recaman(int(sys.argv[1]))
except IndexError:
    print('invalid input!\ntry: python3 recaman.py 20')
    raise SystemExit
