import pandas as pd
df = pd.read_csv("GBPZAR.csv")
print(df["Close"][0], df["Close"][len(df) -1])
#for index, row in df.iterrows():
    #space_index = df.at[index, "Datetime"].index(" ")
    #print(df.at[index, "Datetime"][space_index:-9].replace(":", "."))