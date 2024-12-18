import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV
data = pd.read_csv('telecom_churn.csv')# Zmień 'nazwa_pliku.csv' na rzeczywistą nazwę pliku

# Wyświetlenie pierwszych kilku wierszy danych (opcjonalnie)
print(data.head())

data['Total charges'] = data[['Total day charge', 'Total eve charge', 'Total night charge', 'Total intl charge']].sum(axis=1)

# Wyświetlenie średnich wartości
print(data[['Total day calls', 'Total eve calls', 'Total night calls', 'Total charges']].mean())

# Wizualizacja
data[['Total day minutes', 'Total charges']].hist(bins=30, alpha=0.7)
plt.title('Rozkład minut dziennych i wydatków')
plt.xlabel('Minuty / Wydatki')
plt.ylabel('Liczba klientów')
plt.show()
