# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: SimpleLedger
def dry_run_mode():
    """Enable dry-run mode for data mutation operations.
    When enabled, write operations are logged but not executed.
    """
    global _dry_run
    _dry_run = True
    print("Dry-run mode enabled. All write operations will be simulated.")
    return True
