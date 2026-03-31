import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def train_model():
    data = [
        [18, 265, 1, "weight_loss", 1],
        [9, 120, 1, "weight_loss", 0],
        [31, 165, 0, "weight_loss", 1],
        [8, 120, 1, "weight_gain", 0],
        [28, 190, 0, "weight_gain", 1],
        [12, 220, 1, "maintenance", 1]
    ]

    df = pd.DataFrame(data, columns=[
        "protein", "calories", "is_veg", "goal", "label"
    ])

    encoder = LabelEncoder()
    df["goal_encoded"] = encoder.fit_transform(df["goal"])

    X = df[["protein", "calories", "is_veg", "goal_encoded"]]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    return model, encoder, X_test, y_test
