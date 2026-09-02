# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: SimpleLedger
import unittest
from SimpleLedger import Account, Category, Transaction, Ledger

class TestSimpleLedger(unittest.TestCase):
    def test_create_account(self):
        acct = Account("cash", "Операционные")
        self.assertEqual(acct.name, "cash")
        self.assertEqual(acct.category, "Операционные")
        self.assertEqual(acct.balance, 0.0)

    def test_create_category(self):
        cat = Category("Офис", "Операционные")
        self.assertEqual(cat.name, "Офис")
        self.assertEqual(cat.type, "Операционные")

    def test_create_transaction(self):
        tx = Transaction(
            date="2024-01-15",
            amount=1500.0,
            category="Офис",
            counterparty="ООО Ромашка",
            memo="Аренда офиса"
        )
        self.assertEqual(tx.amount, 1500.0)
        self.assertEqual(tx.date, "2024-01-15")

    def test_ledger_add_transaction(self):
        ledger = Ledger()
        ledger.add_transaction(
            Transaction(
                date="2024-01-15",
                amount=1000.0,
                category="Офис",
                counterparty="ООО Ромашка",
                memo="Аренда"
            )
        )
        self.assertEqual(len(ledger.transactions), 1)

    def test_ledger_report(self):
        ledger = Ledger()
        ledger.add_transaction(
            Transaction(
                date="2024-01-15",
                amount=1000.0,
                category="Офис",
                counterparty="ООО Ромашка",
                memo="Аренда"
            )
        )
        report = ledger.report()
        self.assertIn("Отчёт по операциям", report)
        self.assertIn("2024-01-15", report)
        self.assertIn("Аренда", report)

if __name__ == '__main__':
    unittest.main()
