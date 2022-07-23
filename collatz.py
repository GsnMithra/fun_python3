import matplotlib.pyplot as pyp
from matplotlib import style

a = int(input("Enter any number : "))

arrx = list()
arry = list()

while True:
    arry.append(a)
    if(a == 1):
        break
    elif(a % 2 == 0):
        a = a / 2
    elif(a % 2 != 0):
        a = a * 3 + 1

for i in range(0, len(arry)):
    arrx.append(i)

print("\nArray : " + str(list(arry)))
print("\nTotal step-count : " + str(len(arrx)) + '\n')

pyp.style.use('seaborn-dark')
pyp.plot(arrx, arry)
pyp.show()
