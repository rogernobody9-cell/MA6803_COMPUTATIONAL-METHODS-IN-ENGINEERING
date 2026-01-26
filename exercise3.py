import numpy as np
import matplotlib.pyplot as plt

Matrix_A = np.array([[4, 4, 1],
                    [6, -3, -2],
                    [5, 9, 3]])
Matrix_X = np.array([[6, 2],
                    [-2, 5],
                    [-1, 3]])
Matrix_B = Matrix_A @ Matrix_X
print(f'Matrix_B:\n{Matrix_B}')

fig,ax = plt.subplots()
cax = ax.matshow(Matrix_B, cmap = 'Oranges')
for (i,j),value in np.ndenumerate(Matrix_B):
    ax.text(j,i,
            f'{value}',
            ha='center',
            va='center',
            fontsize=15,
            color='black')
ax.set_title(f'Matrix Multiplication Result\n{Matrix_B.shape}',pad=20)
ax.set_xticks([])
ax.set_yticks([])
plt.show()