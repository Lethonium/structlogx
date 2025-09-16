import logging
import os
from time import time
from pythonjsonlogger import jsonlogger

def init_logger():
    # Get log level from environment variable (default to INFO)
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()

    # Set up the root logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Remove any existing handlers to prevent duplicate logs
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Custom formatter to add epoch timestamp
    class CustomJsonFormatter(jsonlogger.JsonFormatter):
        def add_fields(self, log_record, record, message_dict):
            super().add_fields(log_record, record, message_dict)
            log_record["timestamp"] = time()  # Epoch timestamp
            log_record["filename"] = record.filename  # File name
            log_record["lineno"] = record.lineno  # Line number
            log_record["funcName"] = record.funcName  # Function name

    # # Configure a stream handler with a JSON format
    log_handler = logging.StreamHandler()
    formatter = CustomJsonFormatter('%(asctime)s %(levelname)s %(message)s')
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
