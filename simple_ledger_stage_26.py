# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: SimpleLedger
def run_demo():
    print("=== SimpleLedger Demo ===")
    # categories
    cats = {"salary": "Зарплата", "rent": "Аренда", "food": "Еда"}
    for k, v in cats.items():
        ledger.categories.add(k, v)
    # parties
    ledger.parties.add("ivanov", "+20 000")
    ledger.parties.add("market", "-5000")
    # transactions
    tx1 = Tx(date="2026-01-01", desc="Зарплата", cat="salary", party="ivanov", credit=30000)
    tx2 = Tx(date="2026-01-05", desc="Аренда", cat="rent", party="market", debit=8000)
    tx3 = Tx(date="2026-01-10", desc="Супермаркет", cat="food", party="market", debit=4000)
    ledger.transactions.append(tx1, tx2, tx3)
    # balance report
    print("Balance:")
    for line in ledger.balance_report():
        print(line)
    # summary by category
    print("Summary by category:")
    for line in ledger.category_summary():
        print(line)
    print("Demo finished.")

if __name__ == "__main__":
    run_demo()
