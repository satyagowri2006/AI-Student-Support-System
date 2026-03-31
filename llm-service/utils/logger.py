"""
logger.py

Handles logging for the AI Student Support chatbot.
"""

import logging
from config.settings import LOG_FILE, LOG_LEVEL


# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_info(message: str):
    """
    Log informational messages
    """
    logging.info(message)


def log_warning(message: str):
    """
    Log warning messages
    """
    logging.warning(message)


def log_error(message: str):
    """
    Log error messages
    """
    logging.error(message)