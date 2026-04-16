**PROJECT TITLE: NYC Water Consumption Analysis**

**ONLINE DATASET:** [https://data.cityofnewyork.us/Environment/Water-Consumption-in-the-City-of-New-York/ia2d-e54m/about\_data](https://data.cityofnewyork.us/Environment/Water-Consumption-in-the-City-of-New-York/ia2d-e54m/about_data)

**PYTHON ANALYSIS STEPS**

**STEP 1:** Import Libraries That Will Be Used For Code import pandas as pd import matplotlib.pyplot as plt

**STEP 2:** Load And Clean The Data #Read Water Consumption CSV File df = pd.read\_csv("Water\_Consumption\_NYC\_2026.csv") #Preview Original Dataset print(df.head()) print(df.info()) print(df.describe()) print(df.columns) print(df.isnull().sum()) print(df.duplicated().sum())

**STEP 3:** Filter Data By Year And Remove Null Objects + Duplicates #Filter Year and Remove Duplicates and Null Objects df = df\[df\['Year'\] >= 2000\] print(df.head()) df = df.drop\_duplicates() print(df.duplicated().sum())

**STEP 4:** Create Comparison Table #Create Comparison Table comparison = df\[\[ 'Year', 'NYC Consumption(Million gallons per day)', 'New York City Population', 'Per Capita(Gallons per person per day)' \]\]

print("\\nComparison Table:") print(comparison)

**STEP 5:** Plot Graphs Using Different Key Factors to Visualize Trends #Plot Graphs to Visualize Trends Between Different Factors #Graph 1 plt.figure() plt.plot( df\['Year'\], df\['NYC Consumption(Million gallons per day)'\] ) plt.xlabel('Year') plt.ylabel('NYC Water Consumption (Million Gallons/Day)') plt.title('NYC Water Consumption Over Time') plt.show()

#Graph 2 plt.figure() plt.plot( df\['Year'\], df\['NYC Consumption(Million gallons per day)'\] )

plt.xlabel('Year') plt.ylabel('Water Consumption (Million Gallons/Day)') plt.title('NYC Water Consumption Over Time')

plt.show()

#Graph 3 plt.figure() plt.plot( df\['Year'\], df\['Per Capita(Gallons per person per day)'\] ) plt.xlabel('Year') plt.ylabel('Gallons per Person Per Day') plt.title('Per Capita Water Usage Over Time') plt.show()

#Graph 4 plt.figure() plt.plot( df\['Year'\], df\['New York City Population'\] ) plt.xlabel('Year') plt.ylabel('Population') plt.title('NYC Population Growth Over Time') plt.show()
