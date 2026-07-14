# === Stage 17: Добавь группировку записей по категориям ===
# Project: SimpleLedger
def group_by_category(records):
    """Группирует записи по категориям, суммируя дебет/кредит."""
    grouped = {}
    for r in records:
        cat = r.get("category", "Uncategorized")
        if cat not in grouped:
            grouped[cat] = {"debit": 0, "credit": 0, "count": 0}
        grouped[cat]["debit"] += r["debit"]
        grouped[cat]["credit"] += r["credit"]
        grouped[cat]["count"] += 1
    return grouped
