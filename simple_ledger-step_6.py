# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: SimpleLedger
class LedgerFilter:
    def __init__(self, ledger):
        self.ledger = ledger
    
    def filter_by_status(self, status=None):
        if status is None:
            return list(self.ledger.transactions)
        return [t for t in self.ledger.transactions if t.status == status]
    
    def filter_by_category(self, category_id=None):
        if category_id is None:
            return list(self.ledger.transactions)
        cat = next((c for c in self.ledger.categories if c.id == category_id), None)
        if not cat:
            return []
        return [t for t in self.ledger.transactions if t.category_id == category_id]
    
    def filter_by_tag(self, tag=None):
        if tag is None:
            return list(self.ledger.transactions)
        tags = {c.tags.get(tag) for c in self.ledger.categories}
        return [t for t in self.ledger.transactions if any(t.category_id in tags)]
