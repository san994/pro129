import pandas as pd

columns = ["row_name","star_name","distance","mass","radius"]
df1 = pd.read_csv("dwarf_converted.csv",names=columns)
df1 = df1.iloc[1: , :]
del df1["row_name"]

columns = ["star_name","distance","mass","radius","luminosity"]
df2 = pd.read_csv("star_data.csv",names=columns)
df2 = df2.iloc[1: , :]


final = pd.concat([df1, df2],axis=0)

final.to_csv("final.csv",index=True)