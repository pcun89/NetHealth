from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest(
    contamination=0.05,
    random_state=42
)

def detect_anomalies(values):
    if len(values) < 20:
        return []

    X = np.array(values).reshape(-1, 1)

    preds = model.fit_predict(X)

    anomalies = []

    for i, pred in enumerate(preds):
        if pred == -1:
            anomalies.append(i)

    return anomalies