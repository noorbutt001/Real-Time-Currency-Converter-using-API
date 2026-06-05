from sklearn.linear_model import LinearRegression
import numpy as np


class Forecasting:

    @staticmethod
    def predict(df):

        X = np.arange(
            len(df)
        ).reshape(-1, 1)

        y = df["temperature"]

        model = LinearRegression()

        model.fit(X, y)

        next_day = model.predict(
            [[len(df)]]
        )

        return next_day[0]