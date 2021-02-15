
from matplotlib import pyplot as plt
import numpy as np


def main():
    rate = np.load("rates.npy")
    x = np.zeros(256)
    for i in range(1,256):
        x[i] = i

    sum_LBP = sum(rate[0,:])
    plt.bar(x, rate[0,:]/sum_LBP,align = 'center')
    plt.show()

if __name__ == '__main__':
    main()

