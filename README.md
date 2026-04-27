#  Intelligent Receipt Parser 

##  Overview

This project is an OCR-based system that extracts structured information from receipt images and generates a confidence-aware output. It processes semi-structured receipts and converts them into structured JSON along with an expense summary.

---

##  Features

 Image preprocessing (noise removal, thresholding)
 OCR using EasyOCR
 Key field extraction:

   Store name
   Date
   Total amount
 Confidence scoring for extracted fields
 JSON output generation
 Expense summary across receipts

---

##  Project Structure

```
intelligent-receipt-parser/
│── data/                # Input receipt images
│── outputs/             # JSON outputs
│── src/
│   ├── preprocessing.py
│   ├── ocr_engine.py
│   ├── extractor.py
│   ├── confidence.py
│   ├── summary.py
│── main.py
│── requirements.txt
│── .gitignore
│── README.md
```

---

##  Setup Instructions

###  Clone Repository

```
git clone https://github.com/SoftwareTechnology-Hub/intelligent-receipt-parser.git
cd intelligent-receipt-parser
```

---

###  Create Virtual Environment

#### Windows:

```
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux:

```
python3 -m venv venv
source venv/bin/activate
```

---

###  Install Dependencies

```
pip install -r requirements.txt
```

---

##  EasyOCR Not Installed? Fix

If EasyOCR is missing, install manually:

```
pip install easyocr
```

Also install PyTorch (required for EasyOCR):

 Visit: https://pytorch.org/get-started/locally/

OR use:

```
pip install torch torchvision torchaudio
```

---

##  Run the Project

1. Add receipt images inside:

```
data/
```

2. Run:

```
python main.py
```

---

##  Output

### JSON Output Example

```
{
  "store_name": {"value": "ABC Mart", "confidence": 0.92},
  "date": {"value": "12/03/2024", "confidence": 0.88},
  "total_amount": {"value": "500", "confidence": 0.95}
}
```

### Summary Output

```
{
  "total_spend": 5000,
  "transactions": 10,
  "store_summary": {
    "ABC Mart": 2000,
    "XYZ Store": 3000
  }
}
```

---

##  Approach

 Preprocessed images using OpenCV
 Extracted text using EasyOCR
 Applied regex + heuristics for field extraction
 Generated structured JSON output
 Added confidence scoring using OCR scores

---

##  Challenges

Different receipt formats
Blurry / noisy images
Misaligned text

---

##  Future Improvements

Fine-tune OCR model
Use LayoutLM / Donut models
Improve item extraction
Build UI for visualization

---

##  Requirements

Example `requirements.txt`:

```
opencv-python
easyocr
numpy
pandas
pillow
matplotlib
torch
torchvision
torchaudio
```

---

##  Git Commands Used

```
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/SoftwareTechnology-Hub/intelligent-receipt-parser.git
git push -u origin main
```

---

##  Author

Your Name

---

##  Status

 Working prototype completed
 Ready for submission
