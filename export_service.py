import pandas as pd

class ExportService:

    @staticmethod
    def export_excel(df):

        df.to_excel(
            "exports/weather.xlsx",
            index=False
        )