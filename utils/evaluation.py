import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from py2neo import Graph
import os


class Evaluation_time_period:
    # Connect to Neo4j Database
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "9665131011"))

    # Load datasets
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DART_CSV_FILE_PATH = os.path.join(PROJECT_ROOT, "data", "DART_Dataset.csv")
    LUAS_CSV_FILE_PATH = os.path.join(PROJECT_ROOT, "data", "LUAS_Dataset.csv")
    BUS_CSV_FILE_PATH = os.path.join(PROJECT_ROOT, "data", "BUS_Dataset.csv")

    # Load DART dataset with correct encoding
    data = pd.read_csv(DART_CSV_FILE_PATH, encoding='latin1')

    # Preprocessing
    data.dropna(inplace=True)  # Remove rows with missing values
    X = data[['Distance_km', 'Routes Serviced']].copy()
    X['Routes_Count'] = X['Routes Serviced'].apply(lambda x: len(x.split(',')))
    X.drop('Routes Serviced', axis=1, inplace=True)

    # Target variable
    y = data['TravelTime_min']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluate model
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Mean Absolute Error: {mae:.2f} minutes")
