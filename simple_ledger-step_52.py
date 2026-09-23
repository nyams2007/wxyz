# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: SimpleLedger
def export_report_txt(self):
    """Export a concise text report summarizing all ledger data."""
    lines = [
        "SimpleLedger Report",
        "=" * 40,
        "",
        f"Total transactions: {self._tx_count}",
        f"Total income: {self._total_income}",
        f"Total expenses: {self._total_expenses}",
        f"Balance: {self._balance}",
        "",
        "Top categories:",
    ]
    if self._categories:
        lines.append(f"{'Category':<20} {'Income':>15} {'Expenses':>15} {'Net':>15}")
        lines.append("-" * 65)
        for cat in sorted(self._categories, key=lambda c: c['income'] - c['expenses'], reverse=True):
            net = cat['income'] - cat['expenses']
            lines.append(f"{cat['name']:<20} {cat['income']:>15.2f} {cat['expenses']:>15.2f} {net:>15.2f}")
    else:
        lines.append("No categories yet.")
    lines.append("")
    lines.append("Top counterparties:")
    if self._counterparties:
        lines.append(f"{'Counterparty':<20} {'Debt':>15}")
        lines.append("-" * 35)
        for cp in sorted(self._counterparties, key=lambda c: abs(c['balance']), reverse=True)[:10]:
            lines.append(f"{cp['name']:<20} {cp['balance']:>15.2f}")
    else:
        lines.append("No counterparties yet.")
    lines.append("")
    lines.append("Recent transactions:")
    if self._transactions:
        for tx in self._transactions[-5:]:
            lines.append(f"{tx['date']} | {tx['category']} | {tx['counterparty']} | {tx['amount']:+.2f}")
    else:
        lines.append("No transactions yet.")
    return "\n".join(lines)
