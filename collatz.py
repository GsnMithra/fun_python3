import sys
import matplotlib.pyplot as pyp
from matplotlib import style
a = 0

try:
    a = int((sys.argv[1]))
except IndexError:
    print('No input recieved!\ntry: python3 collatz.py 27')
    raise SystemExit

arrx = list()

while True:
    arrx.append(a)
    if(a == 1):
        break
    elif(a % 2 == 0):
        a = a / 2
    elif(a % 2 != 0):
        a = a * 3 + 1

print("\nArray : " + str(list(arrx)))
print("\nTotal step-count : " + str(len(arrx)) + '\n')

pyp.style.use('seaborn-dark')
pyp.plot(arrx)
pyp.show()
