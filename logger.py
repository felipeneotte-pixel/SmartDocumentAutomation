import logging
from pathlib import Path
from config import LOG_DIR

log_file = Path(LOG_DIR) / "automation.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger("SmartAutomation")
