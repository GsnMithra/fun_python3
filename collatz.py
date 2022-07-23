import sys
import matplotlib.pyplot as pyp
from matplotlib import style

a = (sys.argv[1])

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
