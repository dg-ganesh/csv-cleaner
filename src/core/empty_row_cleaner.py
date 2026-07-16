"""
Project : CSV Cleaner
Project ID : 008

Empty Row Cleaner
"""

import pandas as pd

from src.models.processing_result import ProcessingResult


class EmptyRowCleaner:
    """
    Removes completely empty rows from a DataFrame.

    This module is responsible only for empty row removal.
    It performs no other cleaning operations.
    """

    @staticmethod
    def clean(
        dataframe: pd.DataFrame,
        result: ProcessingResult
    ) -> pd.DataFrame:
        """
        Removes completely empty rows.

        Args:
            dataframe:
                DataFrame to clean.

            result:
                ProcessingResult object used to store statistics.

        Returns:
            Cleaned DataFrame.
        """

        original_row_count = len(dataframe)

        cleaned_dataframe = dataframe.dropna(
            axis=0,
            how="all"
        ).reset_index(drop=True)

        cleaned_row_count = len(cleaned_dataframe)

        rows_removed = (
            original_row_count -
            cleaned_row_count
        )

        result.empty_rows_removed = rows_removed
        result.rows_processed = cleaned_row_count

        return cleaned_dataframe

    @staticmethod
    def count_empty_rows(
        dataframe: pd.DataFrame
    ) -> int:
        """
        Counts completely empty rows.

        Args:
            dataframe:
                DataFrame to inspect.

        Returns:
            Number of completely empty rows.
        """

        return int(
            dataframe.isna().all(axis=1).sum()
        )

    @staticmethod
    def has_empty_rows(
        dataframe: pd.DataFrame
    ) -> bool:
        """
        Determines whether the DataFrame
        contains completely empty rows.

        Args:
            dataframe:
                DataFrame to inspect.

        Returns:
            True if empty rows exist.
        """

        return (
            EmptyRowCleaner.count_empty_rows(
                dataframe
            ) > 0
        )


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - EmptyRowCleaner
#
# Public Methods
# - clean()
# - count_empty_rows()
# - has_empty_rows()
#
# Dependencies
# - pandas
# - src.models.processing_result