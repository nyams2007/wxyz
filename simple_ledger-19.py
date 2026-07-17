# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: SimpleLedger
def archive_records(ledger, cutoff_days=365):
    """Archive records older than cutoff_days into a separate list and remove them from active."""
    import datetime
    cutoff = datetime.datetime.now() - datetime.timedelta(days=cutoff_days)
    archived = []
    for rec in ledger.records:
        if isinstance(rec.timestamp, datetime.datetime) and rec.timestamp < cutoff:
            rec.status = "archived"
            archived.append(rec)
    ledger.records = [r for r in ledger.records if not (isinstance(r.timestamp, datetime.datetime) and r.timestamp < cutoff)]
    return archived
