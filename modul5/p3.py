import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([2, 5, 4, 9])

plt.plot(y1, label='Garis 1')
plt.plot(y2, label='Garis 2')
plt.plot(y3, label='Garis 3')

plt.title('Plot dua garis')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

plt.legend()
plt.show()