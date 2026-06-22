# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: SimpleLedger
def delete_record(record_id, table_name):
    if record_id not in records:
        print(f"Ошибка: запись с ID {record_id} в таблице '{table_name}' не найдена.")
        return False
    del records[table_name][record_id]
    print(f"Запись с ID {record_id} успешно удалена из таблицы '{table_name}'.")
    return True

def get_missing_records(table_name):
    missing = []
    for record in records.get(table_name, {}):
        if not record['id']:
            missing.append(record)
    return missing
