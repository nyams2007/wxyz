# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: SimpleLedger
def check_overdue_reminders(self):
    """Проверка просроченных напоминаний: генерирует сообщения о должниках."""
    overdue = []
    for entry in self.entries:
        if not entry.is_payment and entry.due_date and datetime.now() >= entry.due_date:
            diff = (datetime.now() - entry.due_date).days
            if 0 < diff <= entry.days_to_overdue:
                overdue.append({
                    'entry': entry,
                    'days_overdue': diff,
                    'amount': entry.amount
                })
    if not overdue:
        return []
    messages = []
    for item in overdue:
        entry = item['entry']
        name = self.get_counterparty_name(entry.counterparty) or 'Без имени'
        status = 'Должен' if entry.is_debtor else 'Переплатил'
        msg = f"[ПРОСРОЧКА] {name} — статус: {status}, сумма: {entry.amount} руб., просрочено: {item['days_overdue']} дней."
        messages.append(msg)
    return messages
