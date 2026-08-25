from pathlib import Path

BASE_DIR = Path(__file__).parent

INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
TEMP_DIR = BASE_DIR / "temp"
LOG_DIR = BASE_DIR / "logs"

INPUT_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)
TEMP_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

SUPPORTED_EXTENSIONS = [".pdf"]

EXCEL_NAME = "Relatorio.xlsx"

OCR_LANGUAGE = "por"

WINDOW_TITLE = "Smart Document Automation"

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
