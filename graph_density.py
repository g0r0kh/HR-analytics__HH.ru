import time
import matplotlib.pyplot as plt
from base import data
import numpy as np
import pandas as pd
#


s = pd.Series(data.RUR_net_000)
ax = s.plot.kde()

plt.grid()
plt.show()
