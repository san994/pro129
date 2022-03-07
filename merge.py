import pandas as pd
import csv

columns = ["row_name","star_name","distance","mass","radius"]
df = pd.read_csv("dwarf_star_data.csv",names=columns)
df = df.iloc[1: , :]
del df["row_name"]

df = df[df["mass"].notna()]
df = df[df["radius"].notna()]
df = df[df["distance"].notna()]
df = df[df["star_name"].notna()]

temp_planet_mass = df['mass'].tolist()
temp_planet_mass.pop(0)

for planet_mass in temp_planet_mass:
    mass = float(planet_mass)*0.000954588 
    df["mass"] = mass

# converting radius
temp_planet_radius = df['radius'].tolist()
temp_planet_radius.pop(0)

for planet_radius in temp_planet_radius:
    radius = float(planet_radius)*0.102763
    df["radius"] = radius


df.to_csv("dwarf_converted.csv")