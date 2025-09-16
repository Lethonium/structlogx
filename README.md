# structlogx
A lightweight, production-ready JSON logger for Python with built-in structured logging, epoch timestamps, and source context (filename, line number, function name).

## Features

- ✅ Outputs logs in JSON format for easy parsing
- ✅ Automatically includes epoch timestamp (`timestamp`)
- ✅ Adds source context: `filename`, `lineno`, `funcName`
- ✅ Configurable log level via `LOG_LEVEL` environment variable
- ✅ Zero external dependencies beyond `python-jsonlogger`
- ✅ Drop-in replacement for standard `logging` module

## Installation

```bash
pip install structlogx
```

## Usage

```python
import logging
from json_logger import init_logger

# Initialize the logger
init_logger()

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

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `LOG_LEVEL` | `INFO` | Set log level: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |

## Development

To install in development mode:

```bash
pip install -e .
```

## License

MIT