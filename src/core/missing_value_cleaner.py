"""
Project : CSV Cleaner
Project ID : 008

Missing Value Cleaner
"""

import pandas as pd

from src.models.processing_result import ProcessingResult


class MissingValueCleaner:
    """
    Replaces missing values within a DataFrame.

    This module is responsible only for replacing
    missing values. It performs no other cleaning
    operations.
    """

    @staticmethod
    def clean(
        dataframe: pd.DataFrame,
        replacement_value: str,
        result: ProcessingResult
    ) -> pd.DataFrame:
        """
        Replaces all missing values.

        Args:
            dataframe:
                DataFrame to clean.

            replacement_value:
                Value used to replace missing data.

            result:
                Processing statistics.

        Returns:
            Cleaned DataFrame.
        """

        cleaned_dataframe = dataframe.copy(deep=True)

        missing_values = (
            cleaned_dataframe
            .isna()
            .sum()
            .sum()
        )

        cleaned_dataframe = cleaned_dataframe.fillna(
            replacement_value
        )

        result.missing_values_replaced = int(
            missing_values
        )

        return cleaned_dataframe

    @staticmethod
    def count_missing_values(
        dataframe: pd.DataFrame
    ) -> int:
        """
        Counts all missing values.

        Args:
            dataframe:
                DataFrame to inspect.

        Returns:
            Number of missing values.
        """

        return int(
            dataframe
            .isna()
            .sum()
            .sum()
        )

    @staticmethod
    def has_missing_values(
        dataframe: pd.DataFrame
    ) -> bool:
        """
        Determines whether the DataFrame
        contains missing values.

        Args:
            dataframe:
                DataFrame to inspect.

        Returns:
            True if missing values exist.
        """

        return (
            MissingValueCleaner.count_missing_values(
                dataframe
            ) > 0
        )


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - MissingValueCleaner
#
# Public Methods
# - clean()
# - count_missing_values()
# - has_missing_values()
#
# Dependencies
# - pandas
# - src.models.processing_result