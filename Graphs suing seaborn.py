import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

superstore=pd.read_csv("C:/Users/SHRUTHI K/Documents/Sample Superstore.csv")
#print(superstore.columns)  #dtypes gives data types,columns gives column data
#print(superstore.describe(include='all'))  #describes data for all values inside csv
superstore.hist(figsize=(10,20))                #displays all data in csv in histogram
plt.show()

plt.hist(superstore['Profit'])
plt.hist(superstore['Sales'])                   #Displays individual histogram which contains 2 data
plt.show()
#superstore.head()

#boxplot
#superstore.boxplot(by='Region',column='Profit',grid=False)
sns.boxplot(x=superstore["Region"],y=superstore["Sales"],palette="rocket")   #box plot witrh colour
plt.show()

#Pairplot
sns.pairplot(superstore)
plt.show()

