import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('coviddata.csv')
df.drop(['country_code','continent','source','population','rate_14_day'],axis=1,inplace=True)


################### Calculating b and y0 ###########
t=df['indicator']=='confirmed cases'

t1=df['country']=='France'; df1=df[np.logical_and(t1,t)];
t2=df['country']=='Italy'; df2=df[np.logical_and(t2,t)]
t3=df['country']=='United Kingdom'; df3=df[np.logical_and(t3,t)]

c1=df1['daily_count']
c2=df2['daily_count']
c3=df3['daily_count']


c1.add(c2,fill_value=0)
c1.add(c3,fill_value=0)

er=c1.to_numpy(copy=True)

aa=[]
for x in range(60,72):
    aa.append(np.log(er[x]))
# plt.plot(range(len(aa)),aa)
# plt.show()

p=np.polyfit(range(0,12), aa, 1)
print(p)

b=p[0]
y0=np.exp(p[1])

print(b,y0)
#########################################################

################### Bonus part ######################
res=[]
for i in range(0,12):
    res.append(i*b + np.log(y0))

plt.plot(range(len(aa)),aa)
plt.plot(range(len(aa)),res)
plt.show()
####################################################