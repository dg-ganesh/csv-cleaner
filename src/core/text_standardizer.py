"""
Project : CSV Cleaner
Project ID : 008

Text Standardizer
"""

import pandas as pd

from src.models.processing_result import ProcessingResult


class TextStandardizer:
    """
    Standardizes the case of string values within a DataFrame.

    This module is responsible only for text case conversion.
    It performs no other cleaning operations.
    """

    @staticmethod
    def clean(
        dataframe: pd.DataFrame,
        text_case: str,
        result: ProcessingResult
    ) -> pd.DataFrame:
        """
        Standardizes text case.

        Supported options:
            UPPER
            LOWER
            TITLE

        Args:
            dataframe:
                DataFrame to clean.

            text_case:
                Desired text case.

            result:
                Processing statistics.

        Returns:
            Cleaned DataFrame.
        """

        cleaned_dataframe = dataframe.copy(deep=True)

        values_updated = 0

        for column in cleaned_dataframe.columns:

            cleaned_values = []

            for value in cleaned_dataframe[column]:

                cleaned_value = TextStandardizer._convert(
                    value,
                    text_case
                )

                if (
                    isinstance(value, str)
                    and value != cleaned_value
                ):
                    values_updated += 1

                cleaned_values.append(cleaned_value)

            cleaned_dataframe[column] = cleaned_values

        result.text_values_standardized = values_updated

        return cleaned_dataframe

    @staticmethod
    def _convert(
        value,
        text_case: str
    ):
        """
        Converts a single value to the requested text case.
        """

        if not isinstance(value, str):
            return value

        match text_case:

            case "UPPER":
                return value.upper()

            case "LOWER":
                return value.lower()

            case "TITLE":
                return value.title()

            case _:
                return value

    @staticmethod
    def has_text_to_standardize(
        dataframe: pd.DataFrame,
        text_case: str
    ) -> bool:
        """
        Determines whether standardization would
        modify any string values.
        """

        for column in dataframe.columns:

            for value in dataframe[column]:

                if not isinstance(value, str):
                    continue

                if value != TextStandardizer._convert(
                    value,
                    text_case
                ):
                    return True

        return False


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - TextStandardizer
#
# Public Methods
# - clean()
# - has_text_to_standardize()
#
# Dependencies
# - pandas
# - src.models.processing_result