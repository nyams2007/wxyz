# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: SimpleLedger
import json, os
from dataclasses import dataclass, field, asdict
from datetime import date
from typing import List, Dict, Optional

@dataclass
class Category:
    id: int
    name: str
    description: str = ""

@dataclass
class Counterparty:
    id: int
    name: str
    type: str  # 'client' or 'supplier'
    balance: float = 0.0

@dataclass
class Transaction:
    id: int
    date: date
    description: str
    amount: float
    category_id: Optional[int] = None
    counterparty_id: Optional[int] = None
    type: str = 'income'  # income or expense

def get_data_dir() -> str:
    base = os.path.expanduser("~/.simple_ledger")
    if not os.path.exists(base):
        os.makedirs(base)
    return base

class SimpleLedger:
    def __init__(self, data_dir: Optional[str] = None):
        self.data_dir = data_dir or get_data_dir()
        self.categories: Dict[int, Category] = {}
        self.counterparties: Dict[int, Counterparty] = {}
        self.transactions: List[Transaction] = []
        self._load_or_init()

    def _load_or_init(self):
        cat_file = os.path.join(self.data_dir, "categories.json")
        trans_file = os.path.join(self.data_dir, "transactions.json")
        
        if os.path.exists(cat_file):
            with open(cat_file) as f:
                data = json.load(f)
                self.categories.update({c['id']: Category(**c) for c in data})
            
        if os.path.exists(trans_file):
            with open(trans_file) as f:
                data = json.load(f)
                self.transactions = [Transaction(**t) for t in data]

    def add_category(self, name: str, description: str = "") -> Category:
        cat = Category(id=len(self.categories)+1, name=name, description=description)
        self.categories[cat.id] = cat
        return cat

    def add_counterparty(self, name: str, ctype: str, balance: float = 0.0) -> Counterparty:
        cp = Counterparty(id=len(self.counterparties)+1, name=name, type=ctype, balance=balance)
        self.counterparties[cp.id] = cp
        return cp

    def add_transaction(self, date_str: str, desc: str, amount: float, 
                        cat_id: Optional[int] = None, cp_id: Optional[int] = None, 
                        tx_type: str = 'expense') -> Transaction:
        d = date.fromisoformat(date_str)
        t = Transaction(id=len(self.transactions)+1, date=d, description=desc, amount=amount,
                        category_id=cat_id, counterparty_id=cp_id, type=tx_type)
        self.transactions.append(t)
        
        if cp_id and cp_id in self.counterparties:
            cp = self.counterparties[cp_id]
            if tx_type == 'income':
                cp.balance += amount
            else:
                cp.balance -= amount
        
        return t

    def save(self):
        with open(os.path.join(self.data_dir, "categories.json"), 'w') as f:
            json.dump([asdict(c) for c in self.categories.values()], f, indent=2)
        
        with open(os.path.join(self.data_dir, "transactions.json"), 'w') as f:
            json.dump([asdict(t) for t in self.transactions], f, indent=2)

if __name__ == "__main__":
    app = SimpleLedger()
    
    # Demo data
    cat1 = app.add_category("Food", "Daily groceries")
    cat2 = app.add_category("Utilities", "Electricity and water")
    
    client1 = app.add_counterparty("Acme Corp", "client", 5000.0)
    supplier1 = app.add_counterparty("PowerCo", "supplier", -1000.0)
    
    t1 = app.add_transaction("2023-10-01", "Groceries", 45.5, cat_id=cat1.id)
    t2 = app.add_transaction("2023-10-02", "Electricity bill", 120.0, cp_id=supplier1.id, tx_type='expense')
    t3 = app.add_transaction("2023-10-05", "Payment from Acme", 8500.0, cp_id=client1.id, tx_type='income')
    
    print(f"Added {len(app.categories)} categories and {len(app.transactions)} transactions.")
    app.save()
