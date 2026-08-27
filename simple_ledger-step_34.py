# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: SimpleLedger
import copy

class Template:
    def __init__(self, name, category=None, counterparty=None, description='', amount=None, date=None):
        self.name = name
        self.category = category
        self.counterparty = counterparty
        self.description = description
        self.amount = amount
        self.date = date

    def apply(self, ledger):
        if self.date is None:
            self.date = ledger.now()
        amount = self.amount if self.amount is not None else 0
        entry = {
            'date': self.date,
            'description': self.description or f'[{self.name}]',
            'amount': amount,
            'category': self.category,
            'counterparty': self.counterparty,
        }
        if ledger.get_category(self.category):
            entry['category'] = self.category
        if ledger.get_counterparty(self.counterparty):
            entry['counterparty'] = self.counterparty
        ledger.add_entry(entry)

    def copy(self):
        return Template(self.name, self.category, self.counterparty, self.description, self.amount, self.date)

class TemplateManager:
    def __init__(self):
        self.templates = {}

    def add(self, name, **kwargs):
        t = Template(name, **kwargs)
        self.templates[name] = t
        return t

    def get(self, name):
        return self.templates.get(name)

    def remove(self, name):
        return self.templates.pop(name, None)

    def list(self):
        return list(self.templates.keys())
