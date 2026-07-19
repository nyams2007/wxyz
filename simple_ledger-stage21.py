# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: SimpleLedger
class Reminder:
    def __init__(self, title, date_str):
        self.title = title
        self.date = datetime.strptime(date_str, "%Y-%m-%d")
    
    @property
    def is_due(self):
        return datetime.now().date() >= self.date
    
    def __repr__(self):
        status = "due" if self.is_due else f"pending ({self.date})"
        return f"<Reminder '{self.title}' [{status}]>"

def add_reminder(title, date_str):
    reminders.append(Reminder(title, date_str))
    print(f"✅ Напоминание добавлено: {title} на {date_str}")

def show_due_reminders():
    due = [r for r in reminders if r.is_due]
    return "\n".join(str(r) for r in due) if due else "Нет просроченных напоминаний."

reminders = []
