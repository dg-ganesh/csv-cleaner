"""
Project : CSV Cleaner
Project ID : 008

Whitespace Cleaner
"""

import re

import pandas as pd

from src.models.processing_result import ProcessingResult


class WhitespaceCleaner:
    """
    Cleans whitespace within string values.

    This module is responsible only for whitespace cleanup.
    It performs no other cleaning operations.
    """

    @staticmethod
    def clean(
        dataframe: pd.DataFrame,
        result: ProcessingResult
    ) -> pd.DataFrame:
        """
        Cleans whitespace from all string cells.

        Operations performed:
            - Trim leading whitespace
            - Trim trailing whitespace
            - Replace multiple spaces with a single space

        Args:
            dataframe:
                DataFrame to clean.

            result:
                Processing statistics.

        Returns:
            Cleaned DataFrame.
        """

        cleaned_dataframe = dataframe.copy(deep=True)

        spaces_trimmed = 0
        multiple_spaces_removed = 0

        for column in cleaned_dataframe.columns:

            cleaned_values = []

            for value in cleaned_dataframe[column]:

                (
                    cleaned_value,
                    trimmed,
                    compressed,
                ) = WhitespaceCleaner._clean_cell(value)

                cleaned_values.append(cleaned_value)

                if trimmed:
                    spaces_trimmed += 1

                if compressed:
                    multiple_spaces_removed += 1

            cleaned_dataframe[column] = cleaned_values

        result.spaces_trimmed = spaces_trimmed
        result.multiple_spaces_removed = multiple_spaces_removed

        return cleaned_dataframe

    @staticmethod
    def _clean_cell(
        value
    ) -> tuple[object, bool, bool]:
        """
        Cleans a single cell.

        Returns:
            cleaned_value,
            whitespace_trimmed,
            multiple_spaces_removed
        """

        if not isinstance(value, str):
            return value, False, False

        original_value = value

        trimmed_value = value.strip()

        whitespace_trimmed = (
            trimmed_value != original_value
        )

        compressed_value = re.sub(
            r"\s{2,}",
            " ",
            trimmed_value
        )

        multiple_spaces_removed = (
            compressed_value != trimmed_value
        )

        return (
            compressed_value,
            whitespace_trimmed,
            multiple_spaces_removed,
        )

    @staticmethod
    def has_whitespace(
        dataframe: pd.DataFrame
    ) -> bool:
        """
        Determines whether whitespace cleanup
        is required.
        """

        for column in dataframe.columns:

            for value in dataframe[column]:

                if not isinstance(value, str):
                    continue

                if value != value.strip():
                    return True

                if re.search(r"\s{2,}", value):
                    return True

        return False


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - WhitespaceCleaner
#
# Public Methods
# - clean()
# - has_whitespace()
#
# Dependencies
# - pandas
# - re
# - src.models.processing_result