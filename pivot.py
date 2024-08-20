import pandas as pd
import numpy as np
from base import data
import matplotlib.pyplot as plt
a = data.assign(idx=data.groupby('id#7').cumcount()).pivot_table(index='idx', columns='id#7', values='RUR_net_000', aggfunc='sum')

ax = a.plot.kde()

plt.grid()
plt.show()