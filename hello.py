import pandas as pd
df = pd.read_csv("orders.csv")

print(df[df["Country"].str.startswith('C')])
 