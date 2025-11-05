import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="w"
)

def divide(a,b):
    logging.info(f"Divide {a} by {b}")
    try:
        result = a / b
        logging.debug(f"Result {result}")
        return result
    except ZeroDivisionError:
        logging.error(f"Tried to divide {a} by 0")
        return None

divide(10, 2)
divide(10, 0)