import easyocr

reader = easyocr.Reader(['en'])

def extract_text(image):
    results = reader.readtext(image)

    extracted = []
    for (bbox, text, conf) in results:
        extracted.append({
            "text": text,
            "confidence": conf
        })

    return extracted