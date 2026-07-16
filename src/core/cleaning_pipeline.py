"""
Project : CSV Cleaner
Project ID : 008

Cleaning Pipeline
"""

import pandas as pd

from src.core.duplicate_cleaner import DuplicateCleaner
from src.core.empty_column_cleaner import EmptyColumnCleaner
from src.core.empty_row_cleaner import EmptyRowCleaner
from src.core.missing_value_cleaner import MissingValueCleaner
from src.core.text_standardizer import TextStandardizer
from src.core.whitespace_cleaner import WhitespaceCleaner
from src.models.cleaning_options import CleaningOptions
from src.models.processing_result import ProcessingResult


class CleaningPipeline:
    """
    Coordinates execution of all cleaning modules.

    This class contains no cleaning logic.
    It simply executes the selected cleaning
    operations in the approved order.
    """

    @staticmethod
    def execute(
        dataframe: pd.DataFrame,
        options: CleaningOptions,
        result: ProcessingResult
    ) -> pd.DataFrame:
        """
        Executes the selected cleaning operations.

        Args:
            dataframe:
                Source DataFrame.

            options:
                User-selected cleaning options.

            result:
                Processing statistics.

        Returns:
            Cleaned DataFrame.
        """

        cleaned_dataframe = dataframe.copy(deep=True)

        result.rows_scanned = len(cleaned_dataframe)

        if options.remove_duplicate_rows:

            cleaned_dataframe = DuplicateCleaner.clean(
                cleaned_dataframe,
                result
            )

        if options.remove_empty_rows:

            cleaned_dataframe = EmptyRowCleaner.clean(
                cleaned_dataframe,
                result
            )

        if options.remove_empty_columns:

            cleaned_dataframe = EmptyColumnCleaner.clean(
                cleaned_dataframe,
                result
            )

        if (
            options.trim_whitespace
            or options.compress_multiple_spaces
        ):

            cleaned_dataframe = WhitespaceCleaner.clean(
                cleaned_dataframe,
                result
            )

        if options.replace_missing_values:

            cleaned_dataframe = MissingValueCleaner.clean(
                cleaned_dataframe,
                options.replacement_value,
                result
            )

        if options.standardize_text_case:

            cleaned_dataframe = TextStandardizer.clean(
                cleaned_dataframe,
                options.text_case,
                result
            )

        result.rows_processed = len(cleaned_dataframe)

        result.success = True
        result.message = "CSV cleaned successfully."

        return cleaned_dataframe


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - CleaningPipeline
#
# Public Methods
# - execute()
#
# Dependencies
# - pandas
# - src.models.cleaning_options
# - src.models.processing_result
# - src.core.duplicate_cleaner
# - src.core.empty_row_cleaner
# - src.core.empty_column_cleaner
# - src.core.whitespace_cleaner
# - src.core.missing_value_cleaner
# - src.core.text_standardizer