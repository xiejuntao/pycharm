import pandas as pd
# df = pd.DataFrame()
# print(df)

df = pd.read_csv('uk_rain_2014.csv',header=0)
# print(df.head(5))
df.columns = ['water_year','rain_octsep', 'outflow_octsep',
              'rain_decfeb', 'outflow_decfeb', 'rain_junaug', 'outflow_junaug']

print(df[df['rain_octsep']<1000])