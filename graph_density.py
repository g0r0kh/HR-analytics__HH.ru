import time
import pandas as pd
import numpy as np
from base import data
import matplotlib.pyplot as plt



a = data.assign(idx=data.groupby('id#7').cumcount()).pivot_table(index='idx', columns='id#7', values='RUR_net_000', aggfunc='sum')

a.plot.kde(figsize=(9, 6))

plt.gca().set(xlim=(0.0, 400),
              xlabel='salary net, RUR\nуровень дохода на руки, Руб.', ylabel='density, f(x)\nплотность распределения, f(x)')

# figure name
plt.suptitle(f'Density diagram, HH.ru: {data.period[0]}')
plt.title('Диаграмма плотности распределения, \n'
          'источник: HH.ru, Профессия: Аналитик, 2024.')


plt.grid()
plt.show()