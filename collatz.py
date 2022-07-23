import matplotlib.pyplot as pyp
from matplotlib import style

a = int(input("Enter any number : "))

arrx = list()

while True:
    arry.append(a)
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
