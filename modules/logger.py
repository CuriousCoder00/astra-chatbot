import logging

def setup_logger():
    logging.basicConfig(
        filename='bot_activity.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Logger initialized.")

def log_error(message):
    logging.basicConfig(filename='bot_error.log', level=logging.ERROR, format='%(asctime)s - %(message)s')
    logging.error(message)