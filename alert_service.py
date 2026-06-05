class AlertService:

    @staticmethod
    def get_alerts(weather):

        alerts = []

        if weather["wind_speed"] > 20:
            alerts.append(
                "High Wind Alert"
            )

        if "storm" in weather[
            "condition"
        ].lower():
            alerts.append(
                "Storm Warning"
            )

        if "rain" in weather[
            "condition"
        ].lower():
            alerts.append(
                "Rain Expected"
            )

        return alerts