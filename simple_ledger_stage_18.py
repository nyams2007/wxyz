# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: SimpleLedger
class LedgerTag:
    """Represents a tag that can be applied to operations."""
    
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        if not isinstance(new_name, str) or len(new_name.strip()) == 0:
            raise ValueError("Tag name must be a non-empty string")
        self.name = new_name.strip()
    
    def __repr__(self):
        return f"LedgerTag({self.name!r})"


class SimpleLedger:
    """A simple ledger for tracking operations with categories, counterparties, tags and balances."""
    
    def __init__(self):
        self._operations = []
        self._categories = {}
        self._counterparties = {}
        self._tags = {}
        self._balance = 0.0
    
    # --- Balance management ---
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= 0 or amount > self._balance:
            raise ValueError("Invalid withdrawal")
        self._balance -= amount
    
    def get_balance(self):
        return self._balance
    
    # --- Operations ---
    
    def add_operation(self, description, amount, category=None, counterparty=None, tags=None):
        operation = {
            "description": description,
            "amount": amount,
            "category": category,
            "counterparty": counterparty,
            "tags": list(tags) if tags else [],
        }
        self._operations.append(operation)
    
    def get_operations(self):
        return list(self._operations)
    
    # --- Tag management ---
    
    def add_tag(self, name):
        tag = LedgerTag(name)
        self._tags[tag.name] = tag
    
    def remove_tag(self, name):
        if name not in self._tags:
            raise ValueError(f"Tag '{name}' does not exist")
        del self._tags[name]
    
    def get_tags(self):
        return list(self._tags.values())
