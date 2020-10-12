import pandas as pd


df = pd.read_csv('owid-covid-data.csv')  
# print(df.tail())
# print(df.columns)
# df_ir = df.loc[df['location'] == "Iran"]
# print(df_ir)
# print(df_ir["total_deaths"].sum())
ir = df[['location','median_age','aged_65_older','aged_70_older']]
ir = ir.loc[df['location'] == "Iran"]
print(ir)