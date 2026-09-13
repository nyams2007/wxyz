# === Stage 45: Добавь восстановление из резервной копии ===
# Project: SimpleLedger
def restore_from_backup(source_path):
    """Восстановить данные из резервной копии (JSON-файл)."""
    import json
    if not source_path or not os.path.exists(source_path):
        print(f"[SimpleLedger] Ошибка: резервная копия '{source_path}' не найдена.")
        return False
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"[SimpleLedger] Ошибка при чтении резервной копии: {e}")
        return False
    if not isinstance(data, dict):
        print("[SimpleLedger] Ошибка: файл резервной копии имеет неверный формат.")
        return False
    categories = data.get('categories', {})
    counterparties = data.get('counterparties', {})
    balance = data.get('balance', {})
    transactions = data.get('transactions', [])
    if not all(isinstance(v, list) for v in [transactions]) and transactions:
        transactions = []
    print(f"[SimpleLedger] Резервная копия восстановлена: {len(transactions)} транзакций, {len(categories)} категорий, {len(counterparties)} контрагентов.")
    return True
