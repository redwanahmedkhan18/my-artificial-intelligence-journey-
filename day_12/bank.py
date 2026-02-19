class InsufficientFundsError(Exception):
    """Custom Exception for insufficient balance"""
    pass

def transfer_money(balance):
    try:
        amount = input("Enter amount to transfer: ")

        # Validate input type
        if not amount.isdigit():
            raise ValueError("Amount must be a positive integer")

        amount = int(amount)

        # Validate amount
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        # Check sufficient balance
        if amount > balance:
            raise InsufficientFundsError(
                f"Insufficient balance: You have {balance}, tried to transfer {amount}"
            )

        balance -= amount
        print(f"Transfer successful! Remaining balance: {balance}")

    except ValueError as e:
        print(f"Input Error: {e}")

    except InsufficientFundsError as e:
        print(f"Transaction Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")

    finally:
        print("Transaction attempt finished.")

# Example usage
transfer_money(balance=1000)
