# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: SimpleLedger
def fuzzy_search(self, query, field_names):
    """Поиск по нескольким полям без учёта регистра."""
    return [row for row in self.data if any(
        query.lower() in str(getattr(row, f, '')).lower() for f in field_names
    )]
