import numpy as np
import matplotlib.pyplot as plt
from math import sqrt






def D_ij(i: int, j: int) -> int:

    if i == j:
        return 1
    if j - i == 1:
        return -1
    
    return 0





def calculate_x(to_solve: np.ndarray) -> np.ndarray:

    n_rows = np.shape(to_solve)[0]
    n_columns = np.shape(to_solve)[1]


    current_pivot = n_columns-1

    for i in range(n_rows-1, -1, -1):

        for j in range(i-1, -1, -1):
             operator = -1 * (to_solve[j][current_pivot]/to_solve[i][current_pivot])
             to_solve[j][n_columns-1] += operator * to_solve[j][n_columns-1]
        
        current_pivot -= 1


    current_pivot = 0
    for i in range(n_rows):
        to_solve[i][n_columns-1] /= to_solve[i][current_pivot]
        current_pivot += 1


    return to_solve[:, n_columns-1]

















if __name__ == '__main__':

    btcusdt_chart = np.load('btc_price.npy')
    n = len(btcusdt_chart)


    y = np.reshape(btcusdt_chart, (n, 1))

    D = np.array([[D_ij(i, j) for j in range(n)] for i in range(n-1)])

    landa = 1000.0 
    D = D * sqrt(landa)

    A = np.array([[1 if i == j else 0 for j in range(n)] for i in range(n)])
    A = np.vstack((A, D))


    Y = np.vstack((y, np.zeros(shape=(n-1, 1))))

    A_t = np.transpose(A)

    to_solve = np.hstack((np.matmul(A_t, A), np.matmul(A_t, Y)))

    

    print(calculate_x(to_solve))
