import pandas as pd
import sqlite3
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report

# Define parameter grid for RandomForestClassifier
param_grid = {
    'classifier__n_estimators': [50, 100, 200],
    'classifier__max_depth': [5, 10, None],
    'classifier__min_samples_leaf': [1, 2, 4]
}

# Build pipeline with preprocessing and classification
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(random_state=42))
])

print("Loading data from irrigation.db database...")

# Load data from the irrigation.db database
conn = sqlite3.connect('../irrigation.db')
query = """
SELECT humidity, phosphorus, potassium, ph, pump_state 
FROM irrigation_data 
WHERE humidity IS NOT NULL AND ph IS NOT NULL
"""
df = pd.read_sql_query(query, conn)
conn.close()

print(f"Loaded {len(df)} records from database")

# Prepare features and target
X = df[['humidity', 'phosphorus', 'potassium', 'ph']]
y = df['pump_state']

print(f"Features shape: {X.shape}")
print(f"Target distribution: {y.value_counts().to_dict()}")

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")

# Instantiate GridSearchCV
print("Starting hyperparameter tuning with GridSearchCV...")
grid_search = GridSearchCV(
    pipeline, 
    param_grid, 
    cv=5, 
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)

# Fit GridSearchCV on training data
grid_search.fit(X_train, y_train)

# Print best parameters and accuracy
print(f"\nBest parameters found: {grid_search.best_params_}")
print(f"Best cross-validation score: {grid_search.best_score_:.4f}")

# Evaluate on test set
y_pred = grid_search.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)
print(f"Test set accuracy: {test_accuracy:.4f}")

# Detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the best model
model_filename = '../irrigation_model.joblib'
joblib.dump(grid_search.best_estimator_, model_filename)
print(f"\nBest model saved to {model_filename}")

# Feature importance from the best model
feature_names = ['humidity', 'phosphorus', 'potassium', 'ph']
feature_importance = grid_search.best_estimator_['classifier'].feature_importances_

print("\nFeature Importance:")
for name, importance in zip(feature_names, feature_importance):
    print(f"{name}: {importance:.4f}")
