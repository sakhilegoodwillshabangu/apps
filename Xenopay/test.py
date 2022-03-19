import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
df = yf.Ticker("EURZAR=X").history(period = "1d", interval = "1m")
df2 = df.resample("1T").agg({
        "Open":"first", 
        "High":"max", 
        "Low":"min", 
        "Close":"last"
})
df2.to_csv("EURZARX.csv")
x = df2.index
df = pd.read_csv("EURZARX.csv")
#for index, row in df.iterrows():
    #print(df["Datetime"])
    #space_index = df.at[index, "Datetime"].index(" ")
    #x.append(df.at[index, "Datetime"][space_index:-9])
#for index, row in df.iterrows():
    #space_index = df.at[index, "Datetime"].index(" ")
    #x.append(float(df.at[index, "Datetime"][space_index:-9].replace(":", ".")))
print(x)
y1 = df2["Close"]
y2 = df2["Open"]
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
curve1 = ax1.plot(x, y1, label = "Close", color = "b")
curve2 = ax2.plot(x, y2, label = "Open", color = "w")
fig.patch.set_facecolor((72/float(255), 61/float(255), 139/float(255), 1))
ax1.patch.set_facecolor((72/float(255), 61/float(255), 139/float(255), 1))
plt.plot()
ax1.grid(False)
ax2.grid(False)
ax1.axis("off")
ax2.axis("off")
fig.set_dpi(250)
fig.savefig("EURZARX.png")
plt.show()