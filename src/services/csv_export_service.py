"""
Project : CSV Cleaner
Project ID : 008

CSV Export Service
"""

from pathlib import Path

import pandas as pd

from src.services.file_service import FileService


class CSVExportService:
    """
    Exports a DataFrame to a CSV file.

    This module is responsible only for exporting CSV
    files. It performs no validation or cleaning.
    """

    @staticmethod
    def export(
        dataframe: pd.DataFrame,
        source_file: str | Path
    ) -> Path:
        """
        Exports the cleaned DataFrame.

        Args:
            dataframe:
                DataFrame to export.

            source_file:
                Original CSV file.

        Returns:
            Path to the exported CSV file.
        """

        output_path = FileService.build_output_path(
            source_file
        )

        dataframe.to_csv(
            output_path,
            index=False,
            encoding="utf-8"
        )

        return output_path

    @staticmethod
    def export_to(
        dataframe: pd.DataFrame,
        output_file: str | Path
    ) -> Path:
        """
        Exports the DataFrame to a user-specified
        location.

        Args:
            dataframe:
                DataFrame to export.

            output_file:
                Destination CSV file.

        Returns:
            Path to the exported CSV file.
        """

        output_path = Path(output_file)

        FileService.create_directory(
            output_path.parent
        )

        dataframe.to_csv(
            output_path,
            index=False,
            encoding="utf-8"
        )

        return output_path

    @staticmethod
    def can_export(
        output_file: str | Path
    ) -> bool:
        """
        Determines whether the destination directory
        exists or can be created.

        Args:
            output_file:
                Destination CSV file.

        Returns:
            True if export is possible.
        """

        try:

            FileService.create_directory(
                Path(output_file).parent
            )

            return True

        except OSError:

            return False


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - CSVExportService
#
# Public Methods
# - export()
# - export_to()
# - can_export()
#
# Dependencies
# - pathlib
# - pandas
# - src.services.file_service