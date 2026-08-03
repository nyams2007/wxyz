# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: SimpleLedger
def activate_profile(name: str) -> bool:
    """Переключить активный профиль пользователя."""
    if not profiles:
        print("Профили не инициализированы.")
        return False
    name = name.strip()
    for p in profiles:
        if p["name"].strip().lower() == name.lower():
            active_profile = p
            break
    else:
        print(f"Профиль '{name}' не найден.")
        return False

    old_name = ""
    if active_profile is not None:
        old_name = active_profile["name"]
        active_profile["active"] = True

    print(f"Активный профиль изменён: {old_name!r} -> {name!r}")
    return True


activate_profile("Админ")
