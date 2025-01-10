import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Wczytanie danych
data = fetch_california_housing(as_frame=True)
X = data.data
y = data.target

# Eksploracja danych
print("Podsumowanie danych wejściowych:")
print(X.describe())
print("\nPodsumowanie zmiennej docelowej:")
print(y.describe())

# Sprawdzenie brakujących wartości
print("\nBrakujące wartości w danych:")
print(X.isnull().sum())

# Podział na zbiory treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Trening modelu
model = GradientBoostingRegressor(random_state=42, n_estimators=200, learning_rate=0.1, max_depth=5)
model.fit(X_train, y_train)

# Ewaluacja modelu
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMSE: {mse:.2f}")
print(f"R²: {r2:.2f}")

# Wizualizacja wyników z resztami
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6, label='Predykcje', c='blue')
residuals = y_test - y_pred
plt.scatter(y_test, residuals, alpha=0.6, label='Reszty', c='orange')
plt.axhline(y=0, color='red', linestyle='--', label='Linia odniesienia (zero reszt)')
plt.xlabel('Rzeczywiste wartości (y_test)')
plt.ylabel('Przewidywane wartości i reszty (y_pred - y_test)')
plt.title('Rzeczywiste vs Przewidywane wartości z resztami')
plt.legend()
plt.show()

# Histogram reszt (różnica między rzeczywistymi a przewidywanymi wartościami)
plt.figure(figsize=(10, 6))
plt.hist(residuals, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Rozkład reszt')
plt.xlabel('Reszty (y_test - y_pred)')
plt.ylabel('Liczba obserwacji')
plt.show()

# Zapis modelu
joblib.dump(model, 'california_housing_gb_model.joblib')
print("\nModel zapisano jako 'california_housing_gb_model.joblib'")
