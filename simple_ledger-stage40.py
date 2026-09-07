# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: SimpleLedger
import argparse

def build_cli():
    parser = argparse.ArgumentParser(description="SimpleLedger CLI")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("report", help="Show balance report")
    p.add_argument("--period", choices=["daily", "weekly", "monthly"], default="daily")

    p = sub.add_parser("export", help="Export ledger to CSV")
    p.add_argument("output")
    p.add_argument("--format", choices=["csv", "json"], default="csv")

    p = sub.add_parser("add", help="Add a transaction")
    p.add_argument("amount", type=float)
    p.add_argument("--category", default="general")
    p.add_argument("--counterparty", default="cash")
    p.add_argument("--date", default=None)

    return parser.parse_args()

def main():
    args = build_cli()
    if args.command == "report":
        print(f"[report {args.period}]")
    elif args.command == "export":
        print(f"[export {args.format} -> {args.output}]")
    elif args.command == "add":
        print(f"[add] amount={args.amount}, category={args.category}, counterparty={args.counterparty}")
    else:
        parser.print_help()
