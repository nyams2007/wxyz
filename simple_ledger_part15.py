# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: SimpleLedger
def weekly_stats(self):
    """Return dict {week_start: {'total': float, 'count': int}} for every week with operations."""
    weeks = {}
    for op in self.operations:
        date = op.date.replace(hour=0, minute=0, second=0)
        week_key = date - timedelta(days=date.weekday())  # Monday of the same week
        if week_key not in weeks:
            weeks[week_key] = {'total': 0.0, 'count': 0}
        weeks[week_key]['total'] += op.amount
        weeks[week_key]['count'] += 1
    return dict(sorted(weeks.items()))
