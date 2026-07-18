# === Stage 20: Добавь восстановление записей из архива ===
# Project: SimpleLedger
def restore_from_archive(archive_path: str, ledger_db_path: str) -> int:
    """Восстанавливает записи из текстового архива в базу данных."""
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Файл архива не найден: {archive_path}")
        return 0
    
    count = 0
    for line in lines:
        parts = line.split(',')
        if len(parts) != 5:
            continue
        
        try:
            date, description, category, counterparty, amount = [p.strip() for p in parts]
            amount = float(amount)
            
            if category not in CATEGORIES:
                print(f"Неизвестная категория: {category}")
                continue
            
            if counterparty not in PARTNERS:
                print(f"Неизвестный контрагент: {counterparty}")
                continue
            
            transaction_id, amount = insert_transaction(ledger_db_path, date, description, category, counterparty, amount)
            count += 1
        except Exception as e:
            print(f"Ошибка при обработке строки: {e}")
    
    return count

def export_to_archive(ledger_db_path: str, archive_path: str) -> None:
    """Экспортирует все записи в текстовый архив."""
    with open(archive_path, 'w', encoding='utf-8') as f:
        for transaction in get_transactions(ledger_db_path):
            line = f"{transaction['id']},{transaction['date']},{transaction['description']}," \
                   f"{transaction['category']},{transaction['counterparty']},{transaction['amount']}"
            f.write(line + '\n')
