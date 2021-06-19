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


    y = np.zeros(shape=btcusdt_chart.shape)

    D = np.array([[D_ij(i, j) for j in range(len(y))] for i in range(len(y)-1)])

    landa = 1000.0 
    D = D * sqrt(landa)
    print(D, '\n\n')

    A = np.array([[1 if i == j else 0 for j in range(len(y))] for i in range(len(y))])
    A = np.vstack((A, D))

    print(A)



