# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: SimpleLedger
def monthly_statistics():
    months = {}
    for d in dates:
        m = d.strftime('%Y-%m')
        if m not in months:
            months[m] = {'income': 0, 'expense': 0}
        months[m][d.category_type == 'income'] += d.amount
        months[m][d.category_type == 'expense'] += d.amount
    return months
