# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: SimpleLedger
import json, sys
from pathlib import Path

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки в структуру проекта."""
    try:
        data = json.loads(json_string)
        
        # Валидация обязательных полей для предотвращения ошибок при старте
        required_keys = ['categories', 'counterparts', 'transactions']
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Отсутствует обязательное поле в данных: {key}")
        
        # Преобразование списков категорий и контрагентов для удобного доступа (опционально)
        categories = {cat['id']: cat for cat in data.get('categories', [])}
        counterparts = {cnt['id']: cnt for cnt in data.get('counterparts', [])}
        
        return {
            'categories': categories,
            'counterparts': counterparts,
            'transactions': data.get('transactions', []),
            'metadata': data.get('metadata', {})
        }
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON данных: {e}", file=sys.stderr)
        sys.exit(1)

# Пример использования (раскомментируйте для тестирования с реальными данными):
if __name__ == "__main__":
    initial_json = """
    {
      "categories": [
        {"id": 1, "name": "Еда", "type": "expense"},
        {"id": 2, "name": "Зарплата", "type": "income"}
      ],
      "counterparts": [
        {"id": 101, "name": "Магазин 'У дома'", "type": "vendor"},
        {"id": 102, "name": "Работодатель ООО 'Вектор'", "type": "client"}
      ],
      "transactions": [
        {"date": "2023-10-01", "amount": -500.00, "category_id": 1, "counterpart_id": 101, "description": "Покупка продуктов"},
        {"date": "2023-10-05", "amount": 85000.00, "category_id": 2, "counterpart_id": 102, "description": "Выплата зарплаты"}
      ],
      "metadata": {
        "currency": "RUB",
        "start_date": "2023-01-01"
      }
    }
    """
    
    ledger_data = load_initial_data(initial_json)
    print(f"Загружено категорий: {len(ledger_data['categories'])}")
    print(f"Загружено контрагентов: {len(ledger_data['counterparts'])}")
    print(f"Загружено операций: {len(ledger_data['transactions'])}")
