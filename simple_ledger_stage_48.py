# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: SimpleLedger
def _split_long_function(func_name, lines):
    """Split a function into smaller helper functions while preserving its logic."""
    if func_name not in lines:
        return lines

    start_idx = lines.index(func_name)
    end_idx = start_idx + 1
    while end_idx < len(lines) and (lines[end_idx].startswith('    ') or lines[end_idx].startswith('\t') or lines[end_idx].strip() == ''):
        end_idx += 1

    main_body = lines[start_idx:end_idx]
    helpers = [line for line in main_body if line.strip() and not line.startswith('    ') and not line.startswith('\t')]

    if not helpers:
        return lines

    helper_code = '\n'.join(helpers)
    lines.insert(start_idx, helper_code)
    return lines
