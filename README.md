# Random-Forest-Regression
This repository contains a Python script that implements Random Forest Regression to predict fuel efficiency (measured in miles per gallon, mpg) based on car specifications.

# Random Forest Regression Model

## Overview
This repository contains a Python script that implements **Random Forest Regression** to predict fuel efficiency (measured in miles per gallon, `mpg`) based on car specifications. The model is trained using the **Auto-MPG Dataset**.

---

## **Problem Statement**
Fuel efficiency is an important factor in automobile performance. This project aims to develop a **Random Forest Regression** model that predicts a car's **mpg** based on technical specifications such as **horsepower, weight, and cylinders**.

### **Dataset Description**
The dataset used in this project is from [**Kaggle: Auto-MPG Dataset**](https://www.kaggle.com/datasets/uciml/autompg-dataset) and contains the following features:
- **Horsepower**
- **Weight**
- **Cylinders**
- **Displacement**
- **Acceleration**
- **Origin** (Categorical: USA, Europe, Japan)
- **MPG** (Target variable)

---

## **How the Script Works**
1. **Data Loading and Cleaning**:
   - Reads the dataset from a CSV file.
   - Handles missing values in the `horsepower` column (mean imputation).
2. **Feature Encoding**:
   - Converts categorical variables (e.g., `origin`) into numerical format using **one-hot encoding**.
3. **Data Splitting**:
   - Splits the dataset into **training (80%)** and **testing (20%)** sets.
4. **Model Training**:
   - Implements **Random Forest Regression** using `sklearn.ensemble.RandomForestRegressor()`.
   - Fits the model on the training dataset.
5. **Hyperparameter Tuning**:
   - Optimizes parameters like:
     - `n_estimators` (number of trees)
     - `max_depth` (tree depth)
     - `min_samples_split` (minimum samples required for a split)
   - Uses **GridSearchCV** for hyperparameter tuning.
6. **Model Evaluation**:
   - Makes predictions on the test dataset.
   - Evaluates the model using:
     - **Mean Squared Error (MSE)**
     - **R-squared Score (R²)**
7. **Feature Importance**:
   - Identifies the most influential features in predicting fuel efficiency.
8. **Visualization**:
   - Plots **predicted vs. actual mpg** using a scatter plot.

---

## **Dependencies**
Ensure you have the following Python libraries installed:
```sh
pip install numpy pandas matplotlib scikit-learn
```

---

## **How to Run the Script**
1. Clone the repository:
   ```sh
   git clone <repository_url>
   ```
2. Navigate to the project folder:
   ```sh
   cd <project_folder>
   ```
3. Run the Python script:
   ```sh
   python random_forest_regression.py
   ```
4. Follow the output to view predictions and model performance.

---

## **Contributing**
Contributions are welcome! Feel free to fork this repository and submit a pull request with improvements or additional features.


