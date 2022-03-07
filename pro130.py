import pandas as pd

columns =  ["row_name","star_name","distance","mass","radius","luminosity"]
df = pd.read_csv("final.csv",names=columns)
del df["row_name"]

del df["luminosity"]

df.to_csv('main.csv') 