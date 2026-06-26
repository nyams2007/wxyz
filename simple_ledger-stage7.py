# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: SimpleLedger
def sort_entries(entries, key='date'):
    if not entries: return []
    reverse = {'date': False, 'priority': True, 'name': False}.get(key, False)
    def _sort_key(e):
        val = e.get(key, '')
        if isinstance(val, str): return (0, len(val), val.lower())
        if key == 'priority' and not isinstance(val, int): return (1, 999, val)
        return (1, 0, val)
    return sorted(entries, key=_sort_key, reverse=reverse)
