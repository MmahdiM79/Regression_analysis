import numpy as np
import matplotlib.pyplot as plt
from math import sqrt




def D_ij(i: int, j: int) -> int:

    if i == j:
        return 1
    if j - i == 1:
        return -1
    
    return 0





if __name__ == '__main__':

    btcusdt_chart = np.load('btc_price.npy')
    n = len(btcusdt_chart)


    y = np.reshape(btcusdt_chart, (n, 1))

    D = np.array([[D_ij(i, j) for j in range(n)] for i in range(n-1)])

    landa = 1000.0 
    D = D * sqrt(landa)

    A = np.array([[1 if i == j else 0 for j in range(n)] for i in range(n)])
    A = np.vstack((A, D))


    Y = np.vstack((y, np.zeros(shape=(n, 1))))




