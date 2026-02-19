import requests
import logging

logging.basicConfig(level=logging.INFO)

class APIRequestError(Exception):
    """Custom exception for API failures"""
    pass

def fetch_user_data(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    
    try:
        response = requests.get(url, timeout=5)

        # Check HTTP status
        if response.status_code != 200:
            raise APIRequestError(f"API returned status {response.status_code}")

        # Parse JSON
        try:
            data = response.json()
        except ValueError:
            raise APIRequestError("Invalid JSON response from API")

        # Validate required fields
        if "name" not in data or "email" not in data:
            raise APIRequestError("Missing required user fields")

        print(f"User Name: {data['name']}, Email: {data['email']}")
        return data

    except requests.exceptions.Timeout:
        logging.warning("API request timed out")
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error: {e}")
    except APIRequestError as e:
        logging.error(f"API validation error: {e}")
    finally:
        logging.info("API fetch attempt finished")

fetch_user_data(1)
