import time
import matplotlib.pyplot as plt
from base import data
import numpy as np
import pandas as pd


plt.figure(figsize=(9, 6))

x = [data.RUR_net_000]

df = pd.DataFrame(x, index=[''])

df.T.boxplot(vert=False, showfliers=False) # transpose and except outlier values

# figure name
plt.suptitle(f'Box-and-whiskers Salary diagram, HH.ru: {data.period[0]}')
plt.title('Диаграмма ящик с усами, \n'
          'источник: HH.ru, Профессия: Аналитик, 2024.')

# axes name axes limits
plt.gca().set(xlim=(0.0, 400),
              xlabel='salary net, RUR\nуровень дохода на руки, Руб.')


plt.show()