from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

def load_data():
    iris = load_iris()
    X = iris.data
    y = iris.target
    return X, y

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    param_grid = {
        'n_estimators': [50, 100, 150],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
    
    rf_clf = RandomForestClassifier(random_state=42)
    
    grid_search = GridSearchCV(estimator=rf_clf, param_grid=param_grid, cv=5)
    grid_search.fit(X_train, y_train)
    
    best_model = grid_search.best_estimator_

    print("Tham số tốt nhất:", grid_search.best_params_)
    
    y_pred = best_model.predict(X_test)
    print("Độ chính xác trên tập kiểm thử:", accuracy_score(y_test, y_pred))
    
    report = classification_report(y_test, y_pred)
    print("Classification Report:")
    print(report)
    
    return best_model

def save_model(model, filename):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

if __name__ == "__main__":
    X, y = load_data()
    model = train_model(X, y)
    save_model(model, "iris_model.pkl")