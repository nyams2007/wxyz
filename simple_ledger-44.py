# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: SimpleLedger
def backup_ledger(data_file: str, backup_dir: str = ".backups",
                  backup_prefix: str = "ledger",
                  backup_suffix: str = ".bak",
                  max_backups: int = 10) -> str:
    """Сохраняет копию файла данных в папку backup_dir.
    Удаление старых копий, если их больше max_backups."""
    from pathlib import Path
    backup_path = Path(backup_dir)
    backup_path.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    current_name = Path(data_file).name
    backup_filename = f"{backup_prefix}_{timestamp}_{current_name}{backup_suffix}"
    backup_filepath = backup_path / backup_filename
    shutil.copy2(data_file, backup_filepath)
    backups = sorted(backup_path.glob(f"{backup_prefix}_*{backup_suffix}"))
    while len(backups) > max_backups:
        oldest = backups[0]
        oldest.unlink()
        backups = sorted(backup_path.glob(f"{backup_prefix}_*{backup_suffix}"))
    return str(backup_filepath)
