import matplotlib.pyplot as plt
import pandas as pd
from pandas import Timestamp
import matplotlib
import numpy as np
import matplotlib.dates as mdates


plt.rcParams.update({'font.size': 9})

df = pd.read_csv("phd-data.csv", names=['time', 'words'])

print(df.dtypes)

df['time'] = pd.to_datetime(df['time'])

print(df.dtypes)

print(df['time'].tolist())

fig = plt.figure(figsize=(15, 7))

axes = plt.gca()
axes.set_ylim([0, 50000])
axes.set_xlim([Timestamp('2018-10-03 00:00:00'), Timestamp('2018-11-28 00:00:00')])

plt.yticks(np.arange(0, 50000, 2000))
plt.xticks(df['time'].tolist())

plt.plot(df['time'].tolist(), df['words'].tolist())
plt.xticks(rotation=70)
plt.grid()

axes.axvspan(Timestamp('2018-11-07 00:00:00'), Timestamp('2018-11-08 00:00:00'), facecolor='y', alpha=0.3)
axes.axvspan(Timestamp('2018-11-23 00:00:00'), Timestamp('2018-11-28 00:00:00'), facecolor='g', alpha=0.3)


myFmt = mdates.DateFormatter('%a %d-%m')
axes.xaxis.set_major_formatter(myFmt)

# plt.show()
plt.tight_layout()

plt.savefig("images/phd-words.png")
