# -*- coding: utf-8 -*-
"""Notebook1_Manusia Pelupa_ADIKARA2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vobz1iCrbNu-AdssWo9YVzPat7eIXPWR
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

data = pd.read_csv('/content/train_adikara2024.csv')
data.head()

data.info()

data.isnull().sum()

data.describe(include='all')

plt.figure(figsize=(10, 6))
sns.heatmap(data.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values")
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(data['FoodPriceIndex'], kde=True, bins=30, color='blue')
plt.title("Distribusi FoodPriceIndex")
plt.xlabel("FoodPriceIndex")
plt.ylabel("Frekuensi")
plt.show()

plt.figure(figsize=(12, 6))
country_counts = data['Country'].value_counts()
country_counts.plot(kind='bar', color='skyblue')
plt.title("Data Country")
plt.xlabel("Country")
plt.ylabel("Jumlah")
plt.show()

plt.figure(figsize=(10, 6))
numerical_data = data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numerical_data.corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Kolerasi Matrix")
plt.show()

data = data.dropna(subset=['FoodPriceIndex'])
data.isnull().sum()

features = pd.get_dummies(data.drop(columns=['FoodPriceIndex', 'id']), columns=['Country'], drop_first=True)
target = data['FoodPriceIndex']
train_columns = features.columns
features.head()

x = features
y = target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

rf = RandomForestRegressor(random_state=42)
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=3, n_jobs=-1, scoring='neg_mean_squared_error', verbose=2)
grid_search.fit(x_train, y_train)

grid_search.best_params_
best_model = grid_search.best_estimator_

cv_scores = cross_val_score(best_model, features, target, cv=5, scoring='neg_mean_squared_error')
cv_mse = -cv_scores.mean()
cv_std = cv_scores.std()

print(f"Mean Cross-Validasi MSE: {cv_mse}")
print(f"Standar Deviasi CV MSE: {cv_std}")

y_pred = best_model.predict(x_train)
mse = mean_squared_error(y_train, y_pred)
r2 = r2_score(y_train, y_pred)
print("Validasi Mean Squared Error:", mse)
print("Validasi R-squared:", r2)

test_data = pd.read_csv('test_adikara2024_unlabeled.csv')
test_features = pd.get_dummies(test_data.drop(columns=['id']), columns=['Country'], drop_first=True)
test_features = test_features.reindex(columns=train_columns, fill_value=0)
test_features.head()

test_predictions = best_model.predict(test_features)

submission = pd.DataFrame({
    'id': test_data['id'],
    'FoodPriceIndex': test_predictions
})

submission.to_csv('submission_Manusia Pelupa_ADIKARA2024.csv', index=False)
print("'submission_Manusia Pelupa_ADIKARA2024.csv'")

display(submission.head())

y_pred = best_model.predict(x_train)

print("Ukuran y_train:", y_train.shape)
print("Ukuran y_pred:", y_pred.shape)

y_train = y_train.ravel()
y_pred = y_pred.ravel()

plt.figure(figsize=(8, 6))
plt.scatter(y_train, y_pred, alpha=0.5, color='yellow', edgecolors='k')
plt.plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()], 'r--', lw=2)
plt.title("Aktual vs Prediksi Values")
plt.xlabel("Aktual FoodPriceIndex")
plt.ylabel("Prediksi FoodPriceIndex")
plt.show()

best_model = grid_search.best_estimator_
y_pred = best_model.predict(x_test)

def smape(y_true, y_pred):
    return 100 * np.mean(2 * np.abs(y_pred - y_true) / (np.abs(y_true) + np.abs(y_pred)))

smape_score = smape(y_test, y_pred)
print(f"sMAPE Score pada Data Validasi: {smape_score:.4f}%")

test_data = pd.read_csv('test_adikara2024_unlabeled.csv')
test_features = pd.get_dummies(test_data.drop(columns=['id']), columns=['Country'], drop_first=True)
test_features = test_features.reindex(columns=train_columns, fill_value=0)

print("Kolom setelah One-Hot Encoding pada Data Test:")
test_predictions = best_model.predict(test_features)

submission = pd.DataFrame({
    'id': test_data['id'],
    'FoodPriceIndex': test_predictions
})

submission.to_csv('submission_Manusia Pelupa_ADIKARA2024.csv', index=False)
print("'submission_Manusia Pelupa_ADIKARA2024.csv'")

joblib.dump(best_model, 'Model_Manusia Pelupa_ADIKARA2024.pkl')
print("Model berhasil disimpan sebagai 'Model_Manusia Pelupa_ADIKARA2024.pkl'")

loaded_model = joblib.load('Model_Manusia Pelupa_ADIKARA2024.pkl')
test_predictions = loaded_model.predict(test_features)
print("Hasil Prediksi:", test_predictions[:5])