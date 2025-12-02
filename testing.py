from src.custom_exception import CustomException
from src.logger import get_logger
import sys

logger = get_logger(__name__)

def divide_numbers(num1: float, num2: float) -> float:
    try:
        result = num1 / num2
        logger.info(f"Division successful: {num1} / {num2} = {result}")
        return result
    except ZeroDivisionError as e:
        logger.error("Attempted to divide by zero.")
        raise CustomException("Division by zero is not allowed.", sys) from e
    except Exception as e:
        logger.error("An unexpected error occurred during division.")
        raise CustomException("An unexpected error occurred.", sys) from e

if __name__ == "__main__":
    try:
        logger.info("Starting division test cases.")
        print(divide_numbers(10, 2))  # Expected output: 5.
        print(divide_numbers(10, 0))  # This will raise a CustomException
    except CustomException as ce:
        logger.error(f"CustomException caught: {ce}")