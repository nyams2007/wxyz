# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: SimpleLedger
class VersionedData:
    _VERSION = 1

    @classmethod
    def _apply(cls, data: dict) -> dict:
        if data.get("_version") < cls._VERSION:
            data.setdefault("categories", {})
            data.setdefault("parties", {})
            data.setdefault("balances", {})
            data.setdefault("transactions", [])
            data["_version"] = cls._VERSION
        return data

    @classmethod
    def load(cls, data: dict) -> dict:
        return cls._apply(data)
