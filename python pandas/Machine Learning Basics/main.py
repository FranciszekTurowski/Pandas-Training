from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, export_graphviz, plot_tree
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib
import os

# Wczytanie danych
df = pd.read_csv('music.csv')

# Analiza danych
print("\nSprawdzanie brakujących wartości:")
print(df.isnull().sum())

# Przygotowanie danych
X = df.drop(columns=['genre'])
Y = df['genre']

# Sprawdzanie, czy model istnieje
model_filename = 'music-recommender.joblib'
if os.path.exists(model_filename):
    print("\nŁadowanie istniejącego modelu...")
    model = joblib.load(model_filename)
else:
    print("\nTrening nowego modelu...")

    # Trening modelu
    model = DecisionTreeClassifier()

    # Zapis modelu
    joblib.dump(model, model_filename)
    print(f"\nModel zapisany jako {model_filename}")

# Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
model.fit(X_train, y_train)

# Ewaluacja modelu
predictions = model.predict(X_test)
score = accuracy_score(y_test, predictions)
print(f"\nDokładność modelu: {score * 100:.2f}%")

# Walidacja krzyżowa
cross_val_scores = cross_val_score(model, X, Y, cv=3)
print(f"\nŚrednia dokładność z walidacji krzyżowej: {cross_val_scores.mean() * 100:.2f}%")

# Drzewo decyzyjne (Jupyter Notebook)
plot_tree(model, feature_names=['age', 'gender'],
            class_names=sorted(Y.unique()),
            filled=True)