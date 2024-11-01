import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних із CSV
file_path = 'Data.csv'
data = pd.read_csv(file_path)

# Отримання даних для України та США
years = [int(col.split()[0]) for col in data.columns if 'YR' in col]
ukraine_data = data.loc[data['Country Name'] == 'Ukraine', [col for col in data.columns if 'YR' in col]].values.flatten()
usa_data = data.loc[data['Country Name'] == 'United States', [col for col in data.columns if 'YR' in col]].values.flatten()

# Побудова лінійного графіка для України та США
plt.figure(figsize=(10, 5))
plt.plot(years, ukraine_data, marker='o', label='Ukraine')
plt.plot(years, usa_data, marker='o', label='United States')
plt.xlabel('Year')
plt.ylabel('Adjusted savings: CO2 damage (% of GNI)')
plt.title('Adjusted Savings: CO2 Damage as % of GNI (2002-2021)')
plt.xticks(years[::3])
plt.legend()
plt.grid(True)
plt.show()

# Побудова стовпчастої діаграми для України
plt.figure(figsize=(10, 5))
plt.bar(years, ukraine_data, color='skyblue')
plt.xlabel('Year')
plt.ylabel('Adjusted savings: CO2 damage (% of GNI)')
plt.title('Adjusted Savings: CO2 Damage as % of GNI for Ukraine (2002-2021)')
plt.xticks(years[::3])
plt.show()

# Побудова стовпчастої діаграми для США
plt.figure(figsize=(10, 5))
plt.bar(years, usa_data, color='lightcoral')
plt.xlabel('Year')
plt.ylabel('Adjusted savings: CO2 damage (% of GNI)')
plt.title('Adjusted Savings: CO2 Damage as % of GNI for United States (2002-2021)')
plt.xticks(years[::3])
plt.show()

