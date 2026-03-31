"""
settings.py

Central configuration file for the LLM service.
Stores system settings used across the chatbot.
"""

import os


# ===============================
# Project Paths
# ===============================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")


# ===============================
# LLM Configuration
# ===============================

# Default model name (can be changed later)
LLM_MODEL_NAME = "gpt2"

# Maximum tokens for generated responses
MAX_TOKENS = 200

# Response randomness
TEMPERATURE = 0.7


# ===============================
# Language Settings
# ===============================

DEFAULT_LANGUAGE = "en"

SUPPORTED_LANGUAGES = [
    "en",   # English
    "hi",   # Hindi
    "te"    # Telugu
]


# ===============================
# Sentiment Analysis Settings
# ===============================

NEGATIVE_KEYWORDS = [
    "stress",
    "anxiety",
    "depressed",
    "sad",
    "overwhelmed"
]


# ===============================
# Logging Configuration
# ===============================

LOG_LEVEL = "INFO"

LOG_FILE = os.path.join(BASE_DIR, "chatbot.log")


# ===============================
# FAQ Generation Settings
# ===============================

MAX_FAQ_GENERATION = 5


# ===============================
# Debug Mode
# ===============================

DEBUG_MODE = True