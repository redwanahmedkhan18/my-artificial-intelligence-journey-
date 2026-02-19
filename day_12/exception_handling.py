import logging

logging.basicConfig(level=logging.INFO)

def process_order(price, balance):
    try:
        if price <= 0:
            raise ValueError("Invalid price")
        if price > balance:
            raise RuntimeError("Insufficient funds")

        result = balance / price
        return result

    except ValueError as e:
        logging.error(f"Validation error: {e}")

    except RuntimeError as e:
        logging.error(f"Transaction failed: {e}")

    except Exception as e:
        logging.critical(f"Unexpected failure: {e}")

    finally:
        logging.info("Transaction attempt finished")

process_order(500,100)