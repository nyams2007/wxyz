# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: SimpleLedger
def test_edge_cases():
    assert ledger.get_balance() == 0
    assert ledger.get_transactions() == []
    assert ledger.get_categories() == []
    assert ledger.get_counterparties() == []
    assert ledger.get_reports() == []
    assert ledger.get_summary() == {}
