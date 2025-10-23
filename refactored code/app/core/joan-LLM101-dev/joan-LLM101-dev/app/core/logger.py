import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path
from app.core.config import settings

# Log file setup
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "llm101_lab.log"

# Formatter
formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# File handler (with rotation)
file_handler = RotatingFileHandler(
    filename=LOG_FILE,
    maxBytes=5 * 1024 * 1024,  # 5 MB
    backupCount=settings.BACKUP_COUNT_FILES
)
file_handler.setFormatter(formatter)

# Stream handler (console output)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

# Logger setup
logger = logging.getLogger("llm101-lab")
logger.setLevel(getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO))
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.propagate = False  # Prevents duplicate logs
