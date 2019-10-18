#bar

import matplotlib.pyplot as plt

x = [1,2,3,4]
sq= [1,4,9,16]
cu= [1,8,27,64]

width = 0.2

bad_x = [1 - width/2, 2 - width/2, 3 - width/2, 4 - width/2]


plt.bar([elem - width/2 for elem in x],cu,width,label="Cubes")

plt.bar([elem + width/2 for elem in x],sq, width, label="Squares")


plt.legend(loc='best')

plt.show()