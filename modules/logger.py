import logging

def setup_logger():
    logging.basicConfig(
        filename='bot_activity.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Logger initialized.")

def log_error(message):
    logger = logging.getLogger("astra-errors")
    handler = logging.FileHandler('bot_error.log')
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)
    logger.error(message)
    logger.removeHandler(handler)  # Avoid duplicate logs