"""
Project : CSV Cleaner
Project ID : 008

Duplicate Cleaner
"""

import pandas as pd

from src.models.processing_result import ProcessingResult


class DuplicateCleaner:
    """
    Removes duplicate rows from a DataFrame.

    This module performs only duplicate row removal.
    It does not perform any other cleaning operations.
    """

    @staticmethod
    def clean(
        dataframe: pd.DataFrame,
        result: ProcessingResult
    ) -> pd.DataFrame:
        """
        Removes duplicate rows.

        Args:
            dataframe:
                DataFrame to clean.

            result:
                ProcessingResult object used to store statistics.

        Returns:
            Cleaned DataFrame.
        """

        original_row_count = len(dataframe)

        cleaned_dataframe = dataframe.drop_duplicates(
            ignore_index=True
        )

        cleaned_row_count = len(cleaned_dataframe)

        duplicates_removed = (
            original_row_count -
            cleaned_row_count
        )

        result.duplicate_rows_removed = duplicates_removed
        result.rows_processed = cleaned_row_count

        return cleaned_dataframe

    @staticmethod
    def count_duplicates(
        dataframe: pd.DataFrame
    ) -> int:
        """
        Counts duplicate rows without removing them.

        Args:
            dataframe:
                DataFrame to inspect.

        Returns:
            Number of duplicate rows.
        """

        return int(dataframe.duplicated().sum())

    @staticmethod
    def has_duplicates(
        dataframe: pd.DataFrame
    ) -> bool:
        """
        Determines whether duplicate rows exist.

        Args:
            dataframe:
                DataFrame to inspect.

        Returns:
            True if duplicate rows exist.
        """

        return DuplicateCleaner.count_duplicates(dataframe) > 0


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - DuplicateCleaner
#
# Public Methods
# - clean()
# - count_duplicates()
# - has_duplicates()
#
# Dependencies
# - pandas
# - src.models.processing_result