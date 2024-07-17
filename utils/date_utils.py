from datetime import datetime, timedelta


class DateUtils:
    @staticmethod
    def get_formatted_date(days_after: int) -> str:
        after_date = datetime.now() + timedelta(days=days_after)
        return after_date.strftime("%-m/%-d/%Y")
