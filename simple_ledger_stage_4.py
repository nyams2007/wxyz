# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: SimpleLedger
def edit_transaction(tx_id: int, **kwargs) -> dict | None:
    if not kwargs:
        raise ValueError("Нужны хотя бы одно поле для обновления")
    for t in transactions:
        if t.id == tx_id:
            updated = {k: v for k, v in t.__dict__.items() if k != 'id'}
            updated.update(kwargs)
            # Проверка баланса при изменении суммы или типа операции
            old_total = sum(t.balance for t in transactions)
            new_amount = kwargs.get('amount', 0)
            new_type = kwargs.get('type', 'income')
            if (new_type == 'expense' and new_amount < 0) or \
               (new_type == 'income' and new_amount > 0):
                # Корректировка баланса: удаляем старую запись, добавляем новую с новым балансом
                transactions.remove(t)
                t.amount = abs(new_amount) if new_type == 'expense' else new_amount
                t.type = new_type
            elif (new_type != 'income' and new_amount > 0) or \
                 (new_type != 'expense' and new_amount < 0):
                raise ValueError("Некорректное направление потока денег")
            # Пересчет общего баланса после изменения
            total_balance = sum(abs(x.amount) for x in transactions if x.type == 'income') - \
                           sum(abs(x.amount) for x in transactions if x.type == 'expense')
            t.balance = total_balance
            return updated
    raise ValueError(f"Запись с ID {tx_id} не найдена")
