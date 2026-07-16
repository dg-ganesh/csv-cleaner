"""
Project : CSV Cleaner
Project ID : 008

Cleaning Options Model
"""

from dataclasses import dataclass

from src.config import (
    DEFAULT_REPLACEMENT_VALUE,
    TEXT_CASE_OPTIONS,
)


@dataclass
class CleaningOptions:
    """
    Stores all user-selected cleaning options.

    This model contains only application data.
    It does not contain any business logic.
    """

    remove_duplicate_rows: bool = False

    remove_empty_rows: bool = False

    remove_empty_columns: bool = False

    trim_whitespace: bool = False

    compress_multiple_spaces: bool = False

    replace_missing_values: bool = False

    replacement_value: str = DEFAULT_REPLACEMENT_VALUE

    standardize_text_case: bool = False

    text_case: str = TEXT_CASE_OPTIONS[2]

    def validate(self) -> None:
        """
        Validates option values.

        Raises:
            ValueError: If an invalid text case is supplied.
        """

        if self.text_case not in TEXT_CASE_OPTIONS:
            raise ValueError(
                f"Invalid text case option: {self.text_case}"
            )

    def reset(self) -> None:
        """
        Restores all options to their default values.
        """

        self.remove_duplicate_rows = False
        self.remove_empty_rows = False
        self.remove_empty_columns = False
        self.trim_whitespace = False
        self.compress_multiple_spaces = False
        self.replace_missing_values = False
        self.replacement_value = DEFAULT_REPLACEMENT_VALUE
        self.standardize_text_case = False
        self.text_case = TEXT_CASE_OPTIONS[2]


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - CleaningOptions
#
# Public Methods
# - validate()
# - reset()
#
# Dependencies
# - dataclasses
# - src.config