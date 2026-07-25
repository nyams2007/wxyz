# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: SimpleLedger
def parse_date(date_str):
    """Parse a date string in 'YYYY-MM-DD' or 'DD.MM.YYYY' format and return a datetime.date object."""
    try:
        if '-' in str(date_str):
            parts = str(date_str).split('-')
            year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        elif '.' in str(date_str):
            parts = str(date_str).split('.')
            day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        else:
            raise ValueError(f"Unsupported date format: {date_str}")

        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError(f"Invalid date values: day={day}, month={month}")

        return datetime.date(year, month, day)
    except Exception as e:
        raise ValueError(f"Некорректная дата '{date_str}'") from e
