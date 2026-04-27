import re

def extract_fields(ocr_data):
    store_name = ocr_data[0]["text"] if ocr_data else ""

    date = ""
    total = ""

    for item in ocr_data:
        text = item["text"]

        # Date pattern
        if re.search(r'\d{2}/\d{2}/\d{4}', text):
            date = text

        # Total detection
        if "total" in text.lower():
            total = text

    return {
        "store_name": store_name,
        "date": date,
        "total_amount": total
    }