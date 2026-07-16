"""
Project : CSV Cleaner
Project ID : 008

CSV Loader
"""

from pathlib import Path

import pandas as pd


class CSVLoader:
    """
    Loads CSV files into a pandas DataFrame.

    This module is responsible only for loading CSV data.
    It performs no validation, cleaning or exporting.
    """

    @staticmethod
    def load(file_path: str | Path) -> pd.DataFrame:
        """
        Loads a CSV file.

        Args:
            file_path:
                Path to the CSV file.

        Returns:
            pandas.DataFrame

        Raises:
            FileNotFoundError
            PermissionError
            ValueError
            OSError
        """

        path = Path(file_path)

        try:
            dataframe = pd.read_csv(path)

        except FileNotFoundError:
            raise FileNotFoundError(
                f"CSV file not found: {path}"
            )

        except PermissionError:
            raise PermissionError(
                f"Permission denied while reading '{path}'."
            )

        except pd.errors.EmptyDataError:
            raise ValueError(
                "The CSV file is empty."
            )

        except pd.errors.ParserError as error:
            raise ValueError(
                f"Invalid CSV format: {error}"
            )

        except Exception as error:
            raise OSError(
                f"Unable to load CSV file: {error}"
            )

        return dataframe

    @staticmethod
    def row_count(dataframe: pd.DataFrame) -> int:
        """
        Returns the number of rows.
        """

        return len(dataframe)

    @staticmethod
    def column_count(dataframe: pd.DataFrame) -> int:
        """
        Returns the number of columns.
        """

        return len(dataframe.columns)

    @staticmethod
    def is_empty(dataframe: pd.DataFrame) -> bool:
        """
        Returns True if the DataFrame is empty.
        """

        return dataframe.empty

    @staticmethod
    def get_columns(dataframe: pd.DataFrame) -> list[str]:
        """
        Returns the column names.
        """

        return dataframe.columns.tolist()

    @staticmethod
    def copy(dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Returns a deep copy of the supplied DataFrame.
        """

        return dataframe.copy(deep=True)


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - CSVLoader
#
# Public Methods
# - load()
# - row_count()
# - column_count()
# - is_empty()
# - get_columns()
# - copy()
#
# Dependencies
# - pandas
# - pathlib