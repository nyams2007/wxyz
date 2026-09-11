# === Stage 43: Добавь пагинацию длинных списков ===
# Project: SimpleLedger
def paginate(items, page_size=20):
    """Печатает пагинацию списка с навигацией."""
    total_pages = (len(items) + page_size - 1) // page_size
    for i in range(total_pages):
        start = i * page_size
        end = start + page_size
        page = items[start:end]
        print(f"\n--- Страница {i + 1}/{total_pages} ---")
        for item in page:
            print(f"  - {item}")
    print(f"\nВсего: {len(items)} записей, {total_pages} страниц.")
