"""
Centralized logger configuration.

Every module in the project should import this logger instead of using print().
"""

import sys
from pathlib import Path

from loguru import logger

from src.constants import LOG_DIR

LOG_DIR.mkdir(parents=True, exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>"
)

logger.add(
    LOG_DIR / "training.log",
    rotation="5 MB",
    retention="10 days",
    level="DEBUG"
)