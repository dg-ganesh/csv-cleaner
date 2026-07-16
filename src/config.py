"""
Project : CSV Cleaner
Project ID : 008

Application Configuration
"""

from pathlib import Path

# =============================================================================
# Project Information
# =============================================================================

PROJECT_NAME = "CSV Cleaner"
PROJECT_ID = "008"
VERSION = "1.0.0"

# =============================================================================
# Application Settings
# =============================================================================

WINDOW_TITLE = f"{PROJECT_NAME} v{VERSION}"
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
WINDOW_RESIZABLE = False

# =============================================================================
# Supported Files
# =============================================================================

SUPPORTED_FILE_TYPES = [
    ("CSV Files", "*.csv"),
]

SUPPORTED_FILE_EXTENSIONS = [".csv"]

# =============================================================================
# Default Directories
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"
SAMPLES_DIR = DATA_DIR / "samples"

ASSETS_DIR = PROJECT_ROOT / "assets"

ICONS_DIR = ASSETS_DIR / "icons"
IMAGES_DIR = ASSETS_DIR / "images"
TEMPLATES_DIR = ASSETS_DIR / "templates"
FONTS_DIR = ASSETS_DIR / "fonts"

# =============================================================================
# Output Settings
# =============================================================================

OUTPUT_FILE_SUFFIX = "_cleaned"
DEFAULT_OUTPUT_EXTENSION = ".csv"

# =============================================================================
# Missing Value Settings
# =============================================================================

DEFAULT_REPLACEMENT_VALUE = "N/A"

# =============================================================================
# Text Standardization Options
# =============================================================================

TEXT_CASE_UPPER = "UPPER"
TEXT_CASE_LOWER = "LOWER"
TEXT_CASE_TITLE = "TITLE"

TEXT_CASE_OPTIONS = [
    TEXT_CASE_UPPER,
    TEXT_CASE_LOWER,
    TEXT_CASE_TITLE,
]

# =============================================================================
# Status Messages
# =============================================================================

STATUS_READY = "Ready"

STATUS_LOADING = "Loading CSV..."

STATUS_CLEANING = "Cleaning CSV..."

STATUS_SAVING = "Saving cleaned CSV..."

STATUS_COMPLETED = "Completed"

STATUS_FAILED = "Operation Failed"

# =============================================================================
# UI Labels
# =============================================================================

BROWSE_BUTTON_TEXT = "Browse"

CLEAN_BUTTON_TEXT = "Clean CSV"

# =============================================================================
# Processing Summary Labels
# =============================================================================

SUMMARY_ROWS_SCANNED = "Rows Scanned"

SUMMARY_DUPLICATES_REMOVED = "Duplicate Rows Removed"

SUMMARY_EMPTY_ROWS_REMOVED = "Empty Rows Removed"

SUMMARY_EMPTY_COLUMNS_REMOVED = "Empty Columns Removed"

SUMMARY_SPACES_TRIMMED = "Spaces Trimmed"

SUMMARY_MISSING_VALUES_REPLACED = "Missing Values Replaced"

SUMMARY_OUTPUT_FILE = "Output File"

# =============================================================================
# Public Interface
# =============================================================================

# Public Constants
# - Project Information
# - Window Configuration
# - Directory Paths
# - File Settings
# - Text Case Options
# - Status Messages
# - UI Labels
# - Processing Summary Labels

# Dependencies
# - pathlib