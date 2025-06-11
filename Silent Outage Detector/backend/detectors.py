import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def detect_zscore_anomalies(df, column, threshold=3):
    mean = df[column].mean()
    std = df[column].std()
    df["zscore"] = (df[column] - mean) / std
    df["anomaly"] = df["zscore"].abs() > threshold
    return df[["timestamp", column, "anomaly"]]

def detect_isolationforest(df, columns):
    clf = IsolationForest(contamination=0.05)
    X = df[columns].fillna(0)
    df["iforest"] = clf.fit_predict(X)
    df["anomaly"] = df["iforest"] == -1
    return df[["timestamp"] + columns + ["anomaly"]]
