import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('fdc.xlsx')
df['PE']=tuple(df['PE'].astype(np.float))
df['ROE']= tuple(df['ROE'].astype(np.float))
ax = sns.regplot(x='ROE',y='PE',data = df)
plt.show()
