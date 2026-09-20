# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: SimpleLedger
def self_check():
    from SimpleLedger import (
        Account, Category, Counterparty, Operation, Balance, Report,
        SimpleLedger
    )

    ledger = SimpleLedger()

    cat = Category('food', 'Еда')
    cp = Counterparty('ivan', 'Иван')
    acc = Account('cash', 'Наличные')
    ledger.register(cat, cp, acc)

    op1 = Operation('buy', 100, cp, acc, cat)
    op2 = Operation('sell', 200, cp, acc, cat)
    op3 = Operation('transfer', 50, cp, acc, None)
    ledger.record(op1)
    ledger.record(op2)
    ledger.record(op3)

    bal = Balance()
    bal.compute(ledger)

    report = Report()
    report.generate(ledger, bal)

    assert len(ledger.categories) == 1
    assert len(ledger.counterparties) == 1
    assert len(ledger.accounts) == 1
    assert len(ledger.operations) == 3
    assert bal.total_debit == 100
    assert bal.total_credit == 200
    assert report.lines == 3
    assert report.total == 300

    print('=== SimpleLedger Self-Check PASSED ===')
    print(f'Categories: {ledger.categories}')
    print(f'Counterparties: {ledger.counterparties}')
    print(f'Accounts: {ledger.accounts}')
    print(f'Operations: {ledger.operations}')
    print(f'Balance Debit: {bal.total_debit}')
    print(f'Balance Credit: {bal.total_credit}')
    print(f'Report Lines: {report.lines}')
    print(f'Report Total: {report.total}')
    return True
