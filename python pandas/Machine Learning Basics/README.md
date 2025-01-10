# Opis zadania: Przewidywanie cen mieszkań w Kalifornii

Twoim zadaniem jest stworzenie modelu Machine Learning, który przewidzi medianę ceny mieszkań w różnych regionach Kalifornii na podstawie zestawu cech. Wykonanie tego zadania pozwoli Ci nauczyć się, jak zbudować, przeanalizować i ocenić model regresji przy użyciu bardziej zaawansowanych technik. Zadanie wykonaj w pliku `task.py`

# Zbiór danych:

Używamy wbudowanego zbioru danych California Housing Dataset z biblioteki sklearn.
Opis cech w danych:
    MedInc – Mediana dochodów w regionie.
    HouseAge – Średni wiek budynków w regionie.
    AveRooms – Średnia liczba pokoi na gospodarstwo domowe.
    AveBedrms – Średnia liczba sypialni na gospodarstwo domowe.
    Population – Populacja w regionie.
    AveOccup – Średnia liczba mieszkańców na gospodarstwo domowe.
    Latitude – Szerokość geograficzna regionu.
    Longitude – Długość geograficzna regionu.
Zmienne wyjściowa (y): Mediana ceny mieszkań w regionie.

# Kroki do wykonania:

1. Wczytanie danych:
Skorzystaj z biblioteki sklearn.datasets i funkcji fetch_california_housing.
2. Eksploracja danych:
Sprawdź rozkład cech i wartości zmiennej docelowej.
Wyszukaj brakujące wartości i upewnij się, że dane są gotowe do użycia.
3. Podział na zbiory treningowy i testowy:
Podziel dane na zbiór treningowy i testowy, używając train_test_split.
4. Trening modelu:
Wytrenuj model regresji Gradient Boosting (GradientBoostingRegressor) na zbiorze treningowym.
Eksperymentuj z parametrami modelu (np. n_estimators, learning_rate, max_depth).
5. Ocena modelu:
Dokonaj predykcji na zbiorze testowym.
Oblicz metryki: średni błąd kwadratowy (MSE) i współczynnik determinacji (R²).
Wyciągnij wnioski na podstawie tych metryk.
6. Wizualizacja wyników:
Stwórz wykres porównujący rzeczywiste wartości z przewidywanymi.
Stwórz wykres rozkładu reszt, aby zobaczyć błędy modelu.
7. Zapis modelu:
Zapisz model do pliku (joblib.dump), aby można było go ponownie wykorzystać w przyszłości.

# Metryki i analiza:
- MSE (Mean Squared Error): Określa średnią wielkość błędów popełnionych przez model. Im niższa wartość, tym lepiej.
- R² (R-squared): Mierzy, jak dobrze model wyjaśnia zmienność danych. Wartości bliskie 1 oznaczają bardzo dobre dopasowanie.