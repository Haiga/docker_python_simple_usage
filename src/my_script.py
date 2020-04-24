import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.preprocessing import minmax_scale

print('Start ...')

n = 200
x = np.random.uniform(0,1,n)
y = np.random.uniform(0,1,n)


def heat(x, y):
    size_points = x.size
    heat_points = np.zeros(size_points, dtype=np.float32)
    for index_eval in range(size_points):
        sum_distance = 0
        for index_ind in range(size_points):
            sum_distance += math.sqrt(math.pow(x[index_eval] - x[index_ind], 2) + math.pow(y[index_eval] - y[index_ind], 2))
        heat_points[index_eval] = sum_distance
    return heat_points

heat_points = heat(x, y)
scale_heat_point = minmax_scale(heat_points, feature_range=(0,1))

fig, ax = plt.subplots()
s = np.ones(x.size) * 20

#Paramêmtros, x e y são auto explicativos
#c é a cor do ponto
#s é o tamanho do ponto
#cmap é o tipo de cor que será utilizado (plt.cm.jet => frio para quente, mais exemplos abaixo)
##veja mais exemplos abaixo e mais cmap common on em https://matplotlib.org/examples/color/colormaps_reference.html
im = ax.scatter(x, y, c=scale_heat_point, s=s, cmap=plt.cm.jet)

# Add a colorbar
fig.colorbar(im, ax=ax)

# set the color limits - not necessary here, but good to know how.
im.set_clim(0.0, 1.0)
print('Saving file ...')
import os
print(os.listdir('./data/'))
plt.savefig('./data/img.png')
#plt.savefig('./data2/img.png')
#plt.savefig('./data3/img.png')
print('Done!')


