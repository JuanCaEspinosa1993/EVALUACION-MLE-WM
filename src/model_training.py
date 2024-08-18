from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import os
import joblib


def load_data(features_path: str, labels_path: str) -> tuple[pd.DataFrame, pd.Series]:
    features = pd.read_csv(features_path)
    labels = pd.read_csv(labels_path)
    return features, labels

def train_and_evaluate_decision_tree(X_train: pd.DataFrame, y_train: pd.Series, 
                                     X_test: pd.DataFrame, y_test: pd.Series) -> pd.DataFrame:
    
    val_met = pd.DataFrame(columns=['node', 'accuracy'], index=range(3, 25))

    for i in range(3, 25):
        model = DecisionTreeClassifier(max_leaf_nodes=i, random_state=0)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_true=y_test, y_pred=predictions)

        val_met.loc[i] = [i, accuracy]

    return val_met

def get_best_model_params(val_met: pd.DataFrame) -> dict:
    best_row = val_met.loc[val_met['accuracy'].idxmax()]
    best_params = {
        'best_nodes': int(best_row['node']),
        'best_accuracy': best_row['accuracy']
    }
    return best_params

def train_and_save_best_model(X_train: pd.DataFrame, y_train: pd.Series, 
                              best_params: dict, output_dir: str) -> str:
    best_model = DecisionTreeClassifier(max_leaf_nodes=best_params['best_nodes'], random_state=0)
    best_model.fit(X_train, y_train)
    
    os.makedirs(output_dir, exist_ok=True)
    model_path = os.path.join(output_dir, 'model_decision_tree.pkl')
    joblib.dump(best_model, model_path)
    return model_path

def create_model(features_path: str, labels_path: str, output_dir: str, test_size: float = 0.33, random_state: int = 324):
    # Cargar los datos
    X, y = load_data(features_path, labels_path)

    # Dividir los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Entrenar y evaluar el modelo
    val_met = train_and_evaluate_decision_tree(X_train, y_train, X_test, y_test)

    # Obtener los mejores parámetros
    best_params = get_best_model_params(val_met)

    # Entrenar y guardar el mejor modelo
    train_and_save_best_model(X_train, y_train, best_params, output_dir)
