from typing import Optional
import logging
import os
from time import time
from pythonjsonlogger import jsonlogger

def init_logger(log_level: Optional[str] = None) -> None:
    """
    Initialize a structured JSON logger with custom fields and epoch timestamp.

    This function configures the root logger to output logs in JSON format with
    additional contextual fields including timestamp (epoch), filename, line number,
    and function name. It removes any existing handlers to prevent duplicate logs
    and sets the log level from either the provided parameter or the `LOG_LEVEL`
    environment variable (defaults to `'INFO'`).

    Args:
        log_level (Optional[str]): Log level as a string (e.g., `'DEBUG'`, `'INFO'`, `'WARNING'`).
                                 If `None`, defaults to the value of the `LOG_LEVEL`
                                 environment variable, or `'INFO'` if not set.

    Returns:
        None

    Example:
        ```python
        import logging
        from structlogx import init_logger

        # Initialize the logger
        init_logger('DEBUG')

        # Use standard logging
        logging.info("User logged in", extra={"user_id": 123})
        logging.error("Failed to process request", extra={"error_code": 500})
        ```

    Output:
        ```json
        {
          "timestamp": 1726578901.234,
          "levelname": "INFO",
          "message": "User logged in",
          "filename": "app.py",
          "lineno": 10,
          "funcName": "login_handler",
          "user_id": 123
        }
        ```
    """
    # Get log level from parameter or environment variable (default to INFO)
    log_level = log_level if log_level is not None else os.getenv('LOG_LEVEL', 'INFO').upper()

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
