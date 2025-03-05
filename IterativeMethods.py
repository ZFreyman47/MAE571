# Zach Freyman - MAE571 - Homework 2 - Problem 2 - Iterative Method
#%%
import numpy as np
import matplotlib.pyplot as plt

dx = [0.05, 0.01, 0.005]
ls


for j in range(0, len(dx)):
    x = []
    residual =[]
    for i in np.arange(2,2.2,dx[j]):
        res = i**3 + np.sin(i) - np.cosh(i) - ((i**2)/(np.sinh(i))) - 5.016
        residual.append(res)
        x.append(i)
        i+=dx[j]

    print()
    print(f"Dx= {dx[j]}")
    print("x, Residual")
    for i in range(0, len(x)):
        print(f"{x[i]:.2f}", f"{residual[i]:.5}")
        print()

    plt.plot(x, residual, 'o')
    plt.xlabel('x')
    plt.ylabel('Residual')
    plt.grid()
    plt.title(f"Dx= {dx[j]}")
    plt.show()
# %%
dx = [0.01]


for j in range(0, len(dx)):
    x = []
    residual =[]
    for i in np.arange(2.1,2.2,dx[j]):
        res = i**3 + np.sin(i) - np.cosh(i) - ((i**2)/(np.sinh(i))) - 5.016
        residual.append(res)
        x.append(i)
        i+=dx[j]

    print()
    print(f"Dx= {dx[j]}")
    print("x, Residual")
    for i in range(0, len(x)):
        print(f"{x[i]:.2f}", f"{residual[i]:.5}")
        print()

    plt.plot(x, residual, 'o')
    plt.xlabel('x')
    plt.ylabel('Residual')
    plt.grid()
    plt.title(f"Dx= {dx[j]}")
    plt.show()
# %%
