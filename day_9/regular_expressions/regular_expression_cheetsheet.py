import re

# ===============================
# 1️⃣ Input Text
# ===============================
text = """
Hello, my name is Redwan Ahmed.
I live at 221B Baker Street, London, UK.
My office address is 1600 Pennsylvania Avenue, Washington DC, USA.

📞 Phone: +880-1712-345678, Backup: 01718-998877, Intl: +1 415-555-2671
📧 Email: redwan.ai@gmail.com, alt: redwan_2024@outlook.com

🌐 Website: https://redwan.ai, www.example.com
🔐 IP Address: 192.168.1.1
🆔 Passport: AB1234567
🪪 NID: 1234567890123
🧾 SSN_US: 123-45-6789

💰 Salary: $120,000 | ৳ 150000 | €90,000 | £500
📅 DOB: 17-02-1998 | Joined: 2022/06/01

ZIP: 1207 (BD), 94043-1351 (USA)

Order ID: ORD-2026-778899
Transaction ID: TXN998877665544
"""

# ===============================
# 2️⃣ Regex Patterns (FAANG-Ready)
# ===============================
patterns = {
    "Names": r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)+\b',
    "Emails": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
    "Phones_BD": r'(\+880-1\d{3}-\d{6}|01\d{3}-\d{6})',
    "Phones_Intl": r'(\+\d{1,3}[-\s]?\d{2,5}[-\s]?\d{3,6}[-\s]?\d{3,6})',
    "Websites": r'(https?://(?:www\.)?\S+|www\.\S+\.\S+)',
    "IP": r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
    "Passport": r'\b[A-Z]{2}\d{7}\b',
    "NID": r'\b\d{10,17}\b',
    "SSN_US": r'\b\d{3}-\d{2}-\d{4}\b',
    "Dates": r'\b\d{2}[-/]\d{2}[-/]\d{4}\b|\b\d{4}[-/]\d{2}[-/]\d{2}\b',
    "Currency": r'[$৳€£]\s?\d+(?:,\d{3})*(?:\.\d+)?',
    "ZIP": r'\b\d{4}\b|\b\d{5}(?:-\d{4})?\b',
    "OrderID": r'\bORD-\d{4}-\d{6}\b',
    "TransactionID": r'\bTXN\d{12}\b',
    "Addresses": r'\d{1,5}\s[\w\s]{3,50}(Street|St|Road|Rd|Avenue|Ave|Lane|Ln|Boulevard|Blvd)',
    "Countries": r'\b(Bangladesh|USA|UK|United States|Canada|India|Germany|Australia)\b',
    "Cities": r'\b([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)\b'  # optional: combine with NLP for accuracy
}

# ===============================
# 3️⃣ Extraction Engine Function
# ===============================
def extract_all(text, patterns, ignore_case=True):
    extracted = {}
    flags = re.IGNORECASE if ignore_case else 0
    for key, pattern in patterns.items():
        matches = re.findall(pattern, text, flags)
        # Flatten tuples if regex has groups
        flat_matches = []
        for m in matches:
            if isinstance(m, tuple):
                flat_matches.extend([i for i in m if i])
            else:
                flat_matches.append(m)
        extracted[key] = flat_matches
    return extracted

# ===============================
# 4️⃣ Run Extraction
# ===============================
data = extract_all(text, patterns)

# ===============================
# 5️⃣ Display Results
# ===============================
for k, v in data.items():
    print(f"{k:15} → {v}")
