import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('nflx.csv',parse_dates=True,index_col=0)
dr = df.copy()
#df[1:],从第二行到最后一行，df[:-1]从第一行到倒数第二行，values为了访问数据#
dr[1:]=(df[1:]/df[:-1].values)-1
drt = dr['Adj Close'][1:]
mean = drt.mean()
std = drt.std()
plt.hist(drt, bins=20,  facecolor="blue", edgecolor="black", alpha=0.7)
plt.axvline(mean,color='w',linestyle='dashed',linewidth=2)
plt.axvline(std,color='r',linestyle='dashed',linewidth=2)
plt.axvline(-std,color='r',linestyle='dashed',linewidth=2)
plt.show()
