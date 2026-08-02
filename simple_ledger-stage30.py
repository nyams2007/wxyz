# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: SimpleLedger
class Profile:
    def __init__(self, name, currency="RUB", precision=2):
        self.name = name
        self.currency = currency
        self.precision = precision

    def format_balance(self, balance):
        return f"{balance:.{self.precision}f} {self.currency}"

profiles = [Profile("Default")]


def switch_profile(name=None):
    if name is None:
        return profiles[0]
    for p in profiles:
        if p.name == name:
            return p
    raise ValueError(f"Unknown profile: {name}")
