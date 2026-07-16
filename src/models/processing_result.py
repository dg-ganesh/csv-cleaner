"""
Project : CSV Cleaner
Project ID : 008

Processing Result Model
"""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ProcessingResult:
    """
    Stores the outcome of a CSV cleaning operation.

    This model contains only processing data.
    It does not contain any business logic.
    """

    # -------------------------------------------------------------------------
    # File Information
    # -------------------------------------------------------------------------

    input_file: Path | None = None
    output_file: Path | None = None

    # -------------------------------------------------------------------------
    # Processing Statistics
    # -------------------------------------------------------------------------

    rows_scanned: int = 0

    rows_processed: int = 0

    duplicate_rows_removed: int = 0

    empty_rows_removed: int = 0

    empty_columns_removed: int = 0

    spaces_trimmed: int = 0

    multiple_spaces_removed: int = 0

    missing_values_replaced: int = 0

    text_values_standardized: int = 0

    # -------------------------------------------------------------------------
    # Processing Status
    # -------------------------------------------------------------------------

    success: bool = False

    message: str = ""

    errors: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    # -------------------------------------------------------------------------
    # Helper Methods
    # -------------------------------------------------------------------------

    def add_error(self, message: str) -> None:
        """
        Adds an error message to the processing result.
        """

        self.errors.append(message)

    def add_warning(self, message: str) -> None:
        """
        Adds a warning message to the processing result.
        """

        self.warnings.append(message)

    def reset(self) -> None:
        """
        Restores the processing result to its initial state.
        """

        self.input_file = None
        self.output_file = None

        self.rows_scanned = 0
        self.rows_processed = 0

        self.duplicate_rows_removed = 0
        self.empty_rows_removed = 0
        self.empty_columns_removed = 0

        self.spaces_trimmed = 0
        self.multiple_spaces_removed = 0
        self.missing_values_replaced = 0
        self.text_values_standardized = 0

        self.success = False
        self.message = ""

        self.errors.clear()
        self.warnings.clear()


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - ProcessingResult
#
# Public Methods
# - add_error()
# - add_warning()
# - reset()
#
# Dependencies
# - dataclasses
# - pathlib