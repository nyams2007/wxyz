# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: SimpleLedger
def load_from_json(filepath):
    import json
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект корень")
        for key in ['categories', 'counterparts']:
            if key not in data or not isinstance(data[key], list):
                continue
            for item in data[key]:
                if not isinstance(item, dict) or any(k not in item for k in ('name', 'balance' if key == 'categories' else '')):
                    raise ValueError(f"Неверная структура записи в {key}")
        return data
    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return None
