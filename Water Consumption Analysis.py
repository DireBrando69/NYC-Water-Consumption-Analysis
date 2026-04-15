
import pandas as pd
import matplotlib.pyplot as plt


#Read Water Consumption CSV File
df = pd.read_csv("Water_Consumption_NYC_2026.csv")

#Preview Original Dataset
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())

#Filter Year and Remove Duplicates and Null Objects
df = df[df['Year'] >= 2000]
print(df.head())
df = df.drop_duplicates()
print(df.duplicated().sum())

#Create Comparision Table 
comparison = df[[
    'Year',
    'NYC Consumption(Million gallons per day)',
    'New York City Population',
    'Per Capita(Gallons per person per day)'
]]

print("\nComparison Table:")
print(comparison)

#Plot Graphs to Visualize Trends Between Different Factors
#Graph 1
plt.figure()
plt.plot(
    df['Year'],
    df['NYC Consumption(Million gallons per day)']
)
plt.xlabel('Year')
plt.ylabel('NYC Water Consumption (Million Gallons/Day)')
plt.title('NYC Water Consumption Over Time')
plt.show()

#Graph 2
plt.figure()
plt.plot(
    df['Year'], 
    df['NYC Consumption(Million gallons per day)']
)

plt.xlabel('Year')
plt.ylabel('Water Consumption (Million Gallons/Day)')
plt.title('NYC Water Consumption Over Time')

plt.show()

#Graph 3
plt.figure()
plt.plot(
    df['Year'],
    df['Per Capita(Gallons per person per day)']
)
plt.xlabel('Year')
plt.ylabel('Gallons per Person Per Day')
plt.title('Per Capita Water Usage Over Time')
plt.show()

#Graph 4
plt.figure()
plt.plot(
    df['Year'],
    df['New York City Population']
)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('NYC Population Growth Over Time')
plt.show()
