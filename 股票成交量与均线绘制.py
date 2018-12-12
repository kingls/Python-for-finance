import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('nflx.csv',parse_dates=True,index_col=0)

df['25ma']=df['Adj Close'].rolling(window=25,min_periods=0).mean()
rm=df['25ma']
rstd = df['Adj Close'].rolling(window=25,min_periods=0).std()

ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1)
ax1.plot(df.index,df['25ma'])
ax1.plot(df.index,df['Adj Close'])
ax2.bar(df.index,df['Volume'])
plt.show()
