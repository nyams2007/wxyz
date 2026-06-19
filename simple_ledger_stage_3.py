# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: SimpleLedger
class SimpleLedger:
    def __init__(self):
        self._transactions = []
        self._categories = {}
        self._counterparties = {}
    
    def add_category(self, name, type_="income"):
        if not name.strip(): return False
        self._categories[name] = {"type": type_, "balance": 0.0}
        return True
    
    def add_counterparty(self, name):
        if not name.strip(): return False
        self._counterparties[name] = {"name": name, "balance": 0.0}
        return True
    
    def record_transaction(self, category_name, counterparty_name, amount, description=""):
        cat = self._categories.get(category_name)
        cp = self._counterparties.get(counterparty_name)
        if not cat or not cp: return False
        
        cat["balance"] += amount
        cp["balance"] -= amount
        
        tx_id = len(self._transactions) + 1
        self._transactions.append({
            "id": tx_id,
            "category": category_name,
            "counterparty": counterparty_name,
            "amount": round(amount, 2),
            "description": description.strip() or ""
        })
        return True
    
    def get_balance(self):
        total = sum(cat["balance"] for cat in self._categories.values())
        return round(total, 2)
