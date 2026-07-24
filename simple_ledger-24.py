# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: SimpleLedger
def print_ledger_entry(entry):
    """Компактный вывод одной записи с деталями."""
    if entry is None:
        print("Запись не найдена.")
        return
    print(f"ID: {entry['id']}")
    print(f"Дата: {entry.get('date', 'N/A')}")
    print(f"Категория: {entry.get('category', {}).get('name', 'N/A') if entry.get('category') else 'N/A'}")
    print(f"Контрагент: {entry.get('counterparty', {}).get('name', 'N/A') if entry.get('counterparty') else 'N/A'}")
    print(f"Сумма: {entry['amount']}")
    print(f"Баланс после операции: {entry['balance_after']}")
