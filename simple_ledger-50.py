# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: SimpleLedger
def print_balance_report():
    """Выводит итоговый отчёт по балансу и операционной статистике."""
    print("\n=== Баланс ===")
    print(f"  Активы:        {total_assets:>12,.2f}")
    print(f"  Обязательства: {total_liabilities:>12,.2f}")
    print(f"  Собственный капитал: {equity:>12,.2f}")
    print(f"  Итого:         {total_assets + total_liabilities + equity:>12,.2f}")
    print(f"\n=== Операции ===")
    print(f"  Всего: {len(operations):>4} шт.")
    print(f"  Дебет: {sum(o.amount for o in operations if o.is_debit):>12,.2f}")
    print(f"  Кредит: {sum(o.amount for o in operations if o.is_credit):>12,.2f}")
    print(f"\n=== Контрагенты ===")
    for name, balance in sorted(counterparties.items()):
        print(f"  {name:20} {balance:>12,.2f}")
    print(f"\n=== Категории ===")
    for name in categories:
        print(f"  {name}")
    print()
