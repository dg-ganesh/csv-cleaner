"""
Project : CSV Cleaner
Project ID : 008

CSV Validator
"""

from pathlib import Path

from src.services.file_service import FileService


class CSVValidator:
    """
    Validates CSV files before processing.

    This module performs only validation.
    It does not load, modify or save CSV data.
    """

    @staticmethod
    def validate(file_path: str | Path) -> list[str]:
        """
        Performs all validation checks.

        Args:
            file_path:
                Path to the CSV file.

        Returns:
            List of validation errors.
            An empty list indicates the file is valid.
        """

        errors: list[str] = []

        path = Path(file_path)

        errors.extend(CSVValidator.validate_file_exists(path))
        errors.extend(CSVValidator.validate_file_extension(path))
        errors.extend(CSVValidator.validate_file_readable(path))
        errors.extend(CSVValidator.validate_file_not_empty(path))

        return errors

    @staticmethod
    def validate_file_exists(file_path: Path) -> list[str]:
        """
        Validates that the file exists.
        """

        if not FileService.file_exists(file_path):
            return ["Selected file does not exist."]

        return []

    @staticmethod
    def validate_file_extension(file_path: Path) -> list[str]:
        """
        Validates that the file has a supported extension.
        """

        if not FileService.is_supported_file(file_path):
            return ["Unsupported file type. Please select a CSV file."]

        return []

    @staticmethod
    def validate_file_readable(file_path: Path) -> list[str]:
        """
        Validates that the file can be opened for reading.
        """

        if not FileService.file_exists(file_path):
            return []

        try:
            with open(file_path, "r", encoding="utf-8"):
                pass
        except PermissionError:
            return ["Permission denied while reading the file."]
        except OSError:
            return ["Unable to read the selected file."]

        return []

    @staticmethod
    def validate_file_not_empty(file_path: Path) -> list[str]:
        """
        Validates that the file is not empty.
        """

        if not FileService.file_exists(file_path):
            return []

        try:
            if file_path.stat().st_size == 0:
                return ["The selected CSV file is empty."]
        except OSError:
            return ["Unable to determine the file size."]

        return []

    @staticmethod
    def is_valid(file_path: str | Path) -> bool:
        """
        Convenience method.

        Returns:
            True if the file passes all validation checks.
        """

        return len(CSVValidator.validate(file_path)) == 0


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - CSVValidator
#
# Public Methods
# - validate()
# - validate_file_exists()
# - validate_file_extension()
# - validate_file_readable()
# - validate_file_not_empty()
# - is_valid()
#
# Dependencies
# - pathlib
# - src.services.file_service