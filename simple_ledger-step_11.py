# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: SimpleLedger
import json, os

DATA_FILE = "ledger_data.json"

def save_state(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"[ERROR] Не удалось сохранить данные в {DATA_FILE}: {e}")

def load_state():
    if not os.path.exists(DATA_FILE):
        return {"categories": [], "counterparts": [], "transactions": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        print("[WARN] Файл данных повреждён или отсутствует. Начиная с чистого листа.")
        return {"categories": [], "counterparts": [], "transactions": []}

def init_storage():
    if not os.path.exists(DATA_FILE):
        save_state({"categories": [], "counterparts": [], "transactions": []})
