# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: SimpleLedger
import time

class LedgerChangeLog:
    """Compact change-log for every data mutation in SimpleLedger."""
    def __init__(self, max_size: int = 1000):
        self._entries = []
        self._max_size = max_size

    def record(self, action: str, entity: str, detail: str, ts: float = None):
        if ts is None:
            ts = time.time()
        entry = {
            "ts": ts,
            "action": action,
            "entity": entity,
            "detail": detail
        }
        self._entries.append(entry)
        if len(self._entries) > self._max_size:
            self._entries.pop(0)

    def get_recent(self, count: int = 20) -> list:
        return list(self._entries[-count:])

    def clear(self):
        self._entries.clear()
