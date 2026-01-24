import csv
import logging
from pathlib import Path

DATA_FILE = Path("data.csv")
OUTPUT_FILE = Path("cleaned_data.csv")

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data(path):
    if not path.exists():
        raise FileNotFoundError("Dataset not found")

    with open(path, "r") as f:
        return list(csv.DictReader(f))

def clean_data(rows):
    cleaned = []
    for row in rows:
        try:
            age = int(row["age"])
            salary = float(row["salary"])

            if age <= 0 or salary <= 0:
                raise ValueError("Invalid values")

            cleaned.append({
                "name": row["name"],
                "age": age,
                "salary": salary
            })

        except ValueError as e:
            logging.warning(f"Skipping row {row}: {e}")

    return cleaned

def save_data(rows, path):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

def main():
    try:
        logging.info("Pipeline started")

        data = load_data(DATA_FILE)
        cleaned = clean_data(data)
        save_data(cleaned, OUTPUT_FILE)

        logging.info("Pipeline completed successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    main()
