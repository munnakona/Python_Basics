import pandas as pd
df = pd.read_excel(r"/users/munna/Documents/Generative AI/Advance Python/Pandas/data.xlsx")
df
df.shape
df.columns
len(df.columns)

reverse = df[::-1]