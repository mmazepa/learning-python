import pandas as pd

data = pd.read_csv("src/datasets/film.csv", sep=";", header=0, engine="python")
df = pd.DataFrame(data, columns=["Year", "Title", "Subject", "Actor", "Actress"])
df = df.drop(df.index[0])

print(df)
