# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: SimpleLedger
def print_ledger_table(entries):
    """Print a formatted table of ledger entries in the console."""
    if not entries:
        print("No entries to display.")
        return

    def fmt(entry):
        return f"{entry.get('date','')} | {entry.get('category','')} | {entry.get('amount',0):+.2f} | {entry.get('description','')}"

    lines = [fmt(e) for e in entries]
    widths = [len(max(lines, key=len))]
    
    print(f"{'Date':<15}|{'Category':<15}|{'Amount':>10}|{lines[0].split('|')[3]}")
    for line in lines:
        print(line)

if __name__ == "__main__":
    sample = [
        {"date": "2024-01-15", "category": "Income", "amount": 1500.0, "description": "Salary"},
        {"date": "2024-01-16", "category": "Expenses", "amount": -300.0, "description": "Groceries"},
    ]
    print_ledger_table(sample)
