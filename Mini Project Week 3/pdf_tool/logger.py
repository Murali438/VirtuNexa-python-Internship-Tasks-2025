import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/operations.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_action(message):
    logging.info(message)
