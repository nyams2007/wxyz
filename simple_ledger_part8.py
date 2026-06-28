# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: SimpleLedger
def run_cli():
    print("=== SimpleLedger CLI ===")
    while True:
        cmd = input("\nКоманда (add, categories, partners, balance, reports, quit): ").strip().lower()
        if not cmd: continue
        try:
            action = {
                "add": lambda: add_transaction(),
                "categories": lambda: list_categories(),
                "partners": lambda: list_partners(),
                "balance": lambda: show_balance(),
                "reports": lambda: generate_reports(),
                "quit": lambda: None,
            }[cmd] or print("Неизвестная команда.")
        except KeyError:
            print("Ошибка команды.")
        else:
            if action(): break
