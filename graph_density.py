import time
import matplotlib.pyplot as plt
from base import data
import numpy as np
import pandas as pd
#
# >>> df = pd.DataFrame({
# ...     'x': [1, 2, 2.5, 3, 3.5, 4, 5],
# ...     'y': [4, 4, 4.5, 5, 5.5, 6, 6],
# ... })
# >>> ax = df.plot.kde()
# data[data['year'] != 19]

a = data[data['id#7'] == 'noExperience']
b = data[data['id#7'] == 'between1And3']
c = data[data['id#7'] == 'between3And6']
d = data[data['id#7'] == 'moreThan6']


s = pd.Series(a.RUR_net_000)
ax = s.plot.kde()

plt.grid()
plt.show()
