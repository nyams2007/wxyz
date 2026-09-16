# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: SimpleLedger
def demo():
    print("=== SimpleLedger Demo ===")
    ledger = SimpleLedger()
    cat = ledger.add_category("Офис")
    ledger.add_counterparty("ООО Ромашка", cat)
    ledger.add_counterparty("ИП Иванов", cat)
    ledger.add_counterparty("Бухгалтерия", cat)
    print(f"Категорий: {ledger.categories}")
    print(f"Контрагентов: {ledger.counters}")
    ledger.add_transaction(1000, "Поступление", "ООО Ромашка", "Офис")
    ledger.add_transaction(-500, "Расход", "ИП Иванов", "Офис")
    balance = ledger.balance()
    print(f"Баланс: {balance}")
    print(f"История: {ledger.history}")
    report = ledger.report()
    print(f"Отчёт: {report}")
    print("Demo завершён!")
