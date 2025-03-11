# -*- coding: utf-8 -*-
"""Random Forest Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JM3mgORmjXHNIYH89TSSWC-sNDfW-Wum

# **2. Random Forest Regression**

**Problem Statement**  

Predict the fuel efficiency of cars (measured in miles per gallon, `mpg`) based on their technical specifications using the **Auto-MPG Dataset**. Develop a **Random Forest Regression model** to accurately predict `mpg`, optimize the model’s performance through hyperparameter tuning, and evaluate its accuracy using appropriate metrics. Analyze the importance of different features (e.g., horsepower, weight, cylinders) in determining fuel efficiency.

**DatasetLink**: https://www.kaggle.com/datasets/uciml/autompg-dataset

**Instructions**  

1. **Data Loading and Cleaning**  
   - Load the dataset.  
   - Handle missing values in the `horsepower` column (use mean or median imputation).  

2. **Feature Encoding**  
   - Perform one-hot encoding for the `origin` column.  

3. **Splitting the Data**  
   - Split the data into training (80%) and testing (20%) sets.  

4. **Model Training**  
   - Train a Random Forest Regressor with default hyperparameters to predict `mpg`.  

5. **Hyperparameter Tuning**  
   - Perform grid search or random search to optimize parameters like:  
     - `n_estimators`  
     - `max_depth`  
     - `min_samples_split`  

6. **Model Evaluation**  
   - Evaluate the model on the test set using:  
     - Mean Squared Error (MSE)  
     - R² Score  

7. **Feature Importance**  
   - Plot the feature importance to identify the most influential variables for predicting `mpg`.  

8. **Visualization**  
   - Compare predicted vs. actual values for `mpg` using a scatter plot.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("auto-mpg.csv")
df.head()

missing_values_count = df['horsepower'].isnull().sum()
print(f"Number of missing values in 'horsepower' column: {missing_values_count}")

print(df['origin'].unique())

# prompt: apply one hot encoding on car name

# Convert 'horsepower' column to numeric, coercing errors to NaN
df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')

# Fill missing values in 'horsepower' with the mean
df['horsepower'].fillna(df['horsepower'].mean(), inplace=True)

# Perform one-hot encoding on the 'car name' column
df = pd.get_dummies(df, columns=['car name'], prefix='car')

X = df.iloc[:,1:-1].values
y = df.iloc[:,-1].values

y.shape

X.shape

print(df.columns)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

rf_regressor = RandomForestRegressor(random_state=0)
rf_regressor.fit(X_train, y_train)

# Hyperparameter Tuning (using GridSearchCV as an example)
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(estimator=rf_regressor, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search.fit(X_train, y_train)

best_rf_regressor = grid_search.best_estimator_
print(f"Best Hyperparameters: {grid_search.best_params_}")

# Model Evaluation
y_pred = best_rf_regressor.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Feature Importance
feature_importance = best_rf_regressor.feature_importances_