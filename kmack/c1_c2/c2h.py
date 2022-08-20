import pandas as pd

df = pd.read_csv('./gpdata.csv')
cats = list(df["Category"])

for i in range(len(cats)):
    if cats[i] == "1.9":
        print(i)