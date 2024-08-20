import time
import matplotlib.pyplot as plt
from base import data
import numpy as np
import pandas as pd


plt.figure(figsize=(9, 6))

x = [data.RUR_net_000]
# df = pd.DataFrame(x, index=['RUR net [000]'])
df = pd.DataFrame(x, index=[''])

df.T.boxplot(vert=False, showfliers=False) # transpose and except outlier values
# plt.subplots_adjust(left=0.20)
plt.show()