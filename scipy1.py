import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(1, 3, 100)
def f(x):
    return x**3*np.log(x)-6*x*np.sin(x)-12
plt.title('график', fontsize=14)
plt.xlabel ("X" , color='k', fontstyle="italic", fontsize=18, fontfamily="serif")
plt.ylabel("Y", color='k', fontstyle="italic", fontsize=18, fontfamily='serif')
plt.grid()
plt.plot(x, f(x), linewidth=3, c='red')
plt.show()

