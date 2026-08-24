# === Stage 32: Добавь журнал действий пользователя ===
# Project: SimpleLedger
class ActionLog:
    def __init__(self):
        self._log = []
    
    def record(self, action, details=""):
        self._log.append({"action": action, "details": details, "timestamp": time.time()})
    
    def get_log(self):
        return self._log.copy()
    
    def clear(self):
        self._log.clear()
