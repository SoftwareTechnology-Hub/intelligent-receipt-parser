def assign_confidence(field_value, ocr_conf=0.8):
    if not field_value:
        return {"value": "", "confidence": 0.0}

    return {
        "value": field_value,
        "confidence": round(ocr_conf, 2)
    }