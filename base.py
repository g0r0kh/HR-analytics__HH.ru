import pandas as pd
import numpy as np

# import xlsx
data = pd.read_excel('source/source_HR.xlsx',
                     sheet_name='sheet1')
# add[000] dimension
data['RUR_net_000'] = data['RUR_net'].astype(int)/1000

# rename columns
data = data.rename(columns={'id#7':'Experience'})

