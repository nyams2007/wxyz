# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: SimpleLedger
def generate_summary():
    """Генерирует краткую сводку по текущим данным."""
    summary = []
    if categories:
        summary.append(f"Категории: {len(categories)} шт.")
    else:
        summary.append("Категорий: 0")

    if parties:
        summary.append(f"Контрагенты: {len(parties)} шт.")
    else:
        summary.append("Контрагентов: 0")

    if transactions:
        total_amount = sum(t['amount'] for t in transactions)
        latest_date = max(transactions, key=lambda x: x.get('date', '')).get('date', 'N/A')
        summary.append(f"Общий баланс: {total_amount:.2f}")
        summary.append(f"Последняя операция: {latest_date}")
    else:
        summary.append("Операций: 0")

    if balance is not None:
        summary.append(f"Текущий баланс: {balance:.2f}")

    return "\n".join(summary)
