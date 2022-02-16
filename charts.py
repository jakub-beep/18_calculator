import numpy as np
import matplotlib.pyplot as plt
import math


class Draw:
    x = np.linspace(-2 * math.pi, 2 * math.pi, 1000)
    radian_multiples = [-2, -3 / 2, -1, -1 / 2, 0, 1 / 2, 1, 3 / 2, 2]
    radians = [n * math.pi for n in radian_multiples]
    radian_labels = ['$-2\pi$', '$-3\pi/2$', '$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']

    def __init__(self, func, name, range_y):
        self.func = func
        self.name = name
        self.range_y = range_y

    def draw_trig(self):
        y = self.func(Draw.x)
        if self.name == 'tan':
            y[:-1][np.diff(y) < 0] = np.nan
        else:
            pass
        plt.grid()
        plt.xlabel('x')
        plt.ylabel("${}(x)$".format(self.name))
        plt.ylim(self.range_y[0], self.range_y[1])
        plt.xlim(-2 * math.pi, 2 * math.pi)
        plt.xticks(Draw.radians, Draw.radian_labels)
        plt.title("$y = {}(x)$".format(self.name), fontsize=14)
        plt.plot(Draw.x, y)
        plt.show()


sin = Draw(np.sin, 'sin', [-2, 2])
cos = Draw(np.cos, 'cos', [-2, 2])
tan = Draw(np.tan, 'tan', [-10, 10])
