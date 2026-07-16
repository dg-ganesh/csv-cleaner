"""
Project : CSV Cleaner
Project ID : 008

Empty Column Cleaner
"""

import pandas as pd

from src.models.processing_result import ProcessingResult


class EmptyColumnCleaner:
    """
    Removes completely empty columns from a DataFrame.

    This module is responsible only for empty column removal.
    It performs no other cleaning operations.
    """

    @staticmethod
    def clean(
        dataframe: pd.DataFrame,
        result: ProcessingResult
    ) -> pd.DataFrame:
        """
        Removes completely empty columns.

        Args:
            dataframe:
                DataFrame to clean.

            result:
                ProcessingResult object used to store statistics.

        Returns:
            Cleaned DataFrame.
        """

        original_column_count = len(dataframe.columns)

        cleaned_dataframe = dataframe.dropna(
            axis=1,
            how="all"
        )

        cleaned_column_count = len(cleaned_dataframe.columns)

        columns_removed = (
            original_column_count -
            cleaned_column_count
        )

        result.empty_columns_removed = columns_removed

        return cleaned_dataframe

    @staticmethod
    def count_empty_columns(
        dataframe: pd.DataFrame
    ) -> int:
        """
        Counts completely empty columns.

        Args:
            dataframe:
                DataFrame to inspect.

        Returns:
            Number of completely empty columns.
        """

        return int(
            dataframe.isna().all(axis=0).sum()
        )

    @staticmethod
    def has_empty_columns(
        dataframe: pd.DataFrame
    ) -> bool:
        """
        Determines whether the DataFrame
        contains completely empty columns.

        Args:
            dataframe:
                DataFrame to inspect.

        Returns:
            True if completely empty columns exist.
        """

        return (
            EmptyColumnCleaner.count_empty_columns(
                dataframe
            ) > 0
        )


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - EmptyColumnCleaner
#
# Public Methods
# - clean()
# - count_empty_columns()
# - has_empty_columns()
#
# Dependencies
# - pandas
# - src.models.processing_result