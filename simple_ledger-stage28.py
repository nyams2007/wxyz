# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: SimpleLedger
def report_metrics(ledger):
    """Выводит компактный отчёт о состоянии проекта."""
    total = sum(b["balance"] for b in ledger["balances"].values())
    print(f"Баланс: {total:.2f}\n")
    by_cat = {}
    for _, op in ledger["operations"]:
        c = op.get("category", "other")
        by_cat[c] = by_cat.get(c, 0) + op["amount"]
    print(f"По категориям:\n")
    for cat, amt in sorted(by_cat.items()):
        print(f"  {cat}: {amt:.2f}")
    print()
