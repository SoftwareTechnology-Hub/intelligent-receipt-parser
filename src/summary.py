def generate_summary(all_data):
    total_spend = 0
    transactions = len(all_data)
    store_summary = {}

    for data in all_data:
        try:
            amount = float(data["total_amount"]["value"])
        except:
            amount = 0

        total_spend += amount

        store = data["store_name"]["value"]
        if store not in store_summary:
            store_summary[store] = 0

        store_summary[store] += amount

    return {
        "total_spend": total_spend,
        "transactions": transactions,
        "store_summary": store_summary
    }