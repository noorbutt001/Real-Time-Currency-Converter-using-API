import pandas as pd

class TrendAnalysis:

    @staticmethod
    def city_average(df):

        return df.groupby(
            "city"
        )["temperature"].mean()

    @staticmethod
    def hottest_city(df):

        return df.loc[
            df["temperature"].idxmax()
        ]