import os
import json
from src.preprocessing import preprocess_image
from src.ocr_engine import extract_text
from src.extractor import extract_fields
from src.confidence import assign_confidence
from src.summary import generate_summary

DATA_PATH = "data"
OUTPUT_PATH = "outputs"

all_results = []

for file in os.listdir(DATA_PATH):
    image_path = os.path.join(DATA_PATH, file)

    image = preprocess_image(image_path)
    ocr_data = extract_text(image)
    fields = extract_fields(ocr_data)

    result = {
        "store_name": assign_confidence(fields["store_name"]),
        "date": assign_confidence(fields["date"]),
        "total_amount": assign_confidence(fields["total_amount"])
    }

    all_results.append(result)

    with open(f"{OUTPUT_PATH}/{file}.json", "w") as f:
        json.dump(result, f, indent=4)

summary = generate_summary(all_results)

with open(f"{OUTPUT_PATH}/summary.json", "w") as f:
    json.dump(summary, f, indent=4)

print(" Done! Check outputs folder")