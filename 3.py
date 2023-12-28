import pandas as pd
df=pd.read_excel('data.xlsx')

print("first few rows:")
print(df.head())

print("\n summary statistics:")
print(df.describe())

filtered_data=df[df['age']>30]
print("\n filtered dt(age>30):")
print(filtered_data)

sorted_data=df.sort_values(by='salary',ascending=False)
print("\n sorted data(by slary):")
print(sorted_dta)

df['Bonus']=df['salary']*0.1
print("\n data with new column(Bonus):")
df.to_excel('output.xlsx',index=False)
print("\n data written to output.xlsx")
