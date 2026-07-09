from loguru import logger
import sys
import os

os.makedirs("logs", exist_ok=True)

logger.remove()

# Console logging
logger.add(
    sys.stdout,
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

# File logging
logger.add(
    "logs/app.log",
    rotation="5 MB",
    retention="10 days",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)