import pandas as pd
df = pd.read_csv("emp.csv")
print(df.dtypes)

df['doj'] = pd.to_datetime(df['doj'], format="%d/%m/%Y")
print(df)




