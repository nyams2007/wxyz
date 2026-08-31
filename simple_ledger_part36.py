# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: SimpleLedger
def repair_ledger():
    """Compact integrity check + repair. Returns (ok, issues_found, issues_fixed)."""
    issues_found = []
    issues_fixed = []

    # 1. Balance consistency: sum of all operations must equal current balance.
    expected = sum(op.balance for op in ledger.operations)
    if abs(expected - ledger.balance) > 0.01:
        issues_found.append("Balance drift detected.")
        ledger.balance = round(expected, 2)
        issues_fixed.append("Balance corrected.")

    # 2. Category references: every operation's category_id must exist.
    valid_cats = {c.id for c in ledger.categories}
    for op in ledger.operations:
        if op.category_id not in valid_cats:
            issues_found.append(f"Operation #{op.id} has unknown category_id.")
            op.category_id = None
            issues_fixed.append("Orphaned category_id cleared.")

    # 3. Counterparty references: every operation's counterparty_id must exist.
    valid_con = {c.id for c in ledger.countries}
    for op in ledger.operations:
        if op.counterparty_id not in valid_con:
            issues_found.append(f"Operation #{op.id} has unknown counterparty_id.")
            op.counterparty_id = None
            issues_fixed.append("Orphaned counterparty_id cleared.")

    return len(issues_found) == 0, issues_found, issues_fixed
