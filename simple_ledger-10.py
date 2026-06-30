# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: SimpleLedger
def export_to_json():
    import json
    state = {
        "categories": list(categories.values()),
        "counterparts": list(counterparts.values()),
        "transactions": transactions,
        "balance": balance_state.copy() if hasattr(balance_state, 'copy') else dict(balance_state)
    }
    return json.dumps(state, indent=2, ensure_ascii=False)
