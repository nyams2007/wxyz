# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: SimpleLedger
class ValidationError(Exception): pass

def validate_positive(value, name="значение"):
    if not isinstance(value, (int, float)) or value <= 0:
        raise ValidationError(f"{name} должен быть положительным числом")
    return True

def validate_category(category_name: str) -> bool:
    if category_name and len(category_name.strip()) > 0:
        return True
    raise ValidationError("Название категории не может быть пустым")

def validate_counterparty(name: str, contact_info: str = "") -> tuple[bool, str]:
    if not name or len(name) < 2:
        raise ValidationError("Имя контрагента должно содержать минимум 2 символа")
    return True, ""
