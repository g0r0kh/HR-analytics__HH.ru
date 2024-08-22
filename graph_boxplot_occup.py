import time
import matplotlib.pyplot as plt
from base import data
import numpy as np
import pandas as pd

sort_list = sorted(set(data['Occupation']))

occup = []

for i in sort_list:
    a = data[data['Occupation'] == i]
    occup.append(a.RUR_net_000)

fig, ax = plt.subplots(figsize=(11, 9))
plt.subplots_adjust(left=0.45)


# figure name
plt.suptitle(f'Box-and-whiskers Salary diagram, HH.ru: {data.period[0]}')
plt.title('Диаграмма ящик с усами, \n'
          f'источник: HH.ru')
# axes name
ax.set_xlabel('salary net, RUR\nуровень дохода на руки, Руб.')
ax.set_ylabel('occupation\nдолжность')
# data point params
ax.boxplot(occup,patch_artist=True, vert=False, showfliers=False, labels=sort_list)



plt.grid()
plt.show()