"""
Project : CSV Cleaner
Project ID : 008

File Service
"""

from pathlib import Path

from src.config import (
    OUTPUT_DIR,
    OUTPUT_FILE_SUFFIX,
    DEFAULT_OUTPUT_EXTENSION,
    SUPPORTED_FILE_EXTENSIONS,
)


class FileService:
    """
    Provides file-related services for the application.

    This module is responsible only for file operations.
    It contains no business logic.
    """

    @staticmethod
    def file_exists(file_path: str | Path) -> bool:
        """
        Returns True if the specified file exists.
        """

        return Path(file_path).is_file()

    @staticmethod
    def directory_exists(directory: str | Path) -> bool:
        """
        Returns True if the specified directory exists.
        """

        return Path(directory).is_dir()

    @staticmethod
    def create_directory(directory: str | Path) -> None:
        """
        Creates the specified directory if it does not already exist.
        """

        Path(directory).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def is_supported_file(file_path: str | Path) -> bool:
        """
        Checks whether the supplied file has a supported extension.
        """

        extension = Path(file_path).suffix.lower()

        return extension in SUPPORTED_FILE_EXTENSIONS

    @staticmethod
    def get_file_name(file_path: str | Path) -> str:
        """
        Returns the file name including extension.
        """

        return Path(file_path).name

    @staticmethod
    def get_file_stem(file_path: str | Path) -> str:
        """
        Returns the filename without its extension.
        """

        return Path(file_path).stem

    @staticmethod
    def get_file_extension(file_path: str | Path) -> str:
        """
        Returns the file extension.
        """

        return Path(file_path).suffix.lower()

    @staticmethod
    def get_parent_directory(file_path: str | Path) -> Path:
        """
        Returns the parent directory.
        """

        return Path(file_path).parent

    @staticmethod
    def build_output_filename(file_path: str | Path) -> str:
        """
        Creates the cleaned output filename.

        Example:
            sales.csv
            ->
            sales_cleaned.csv
        """

        input_path = Path(file_path)

        return (
            f"{input_path.stem}"
            f"{OUTPUT_FILE_SUFFIX}"
            f"{DEFAULT_OUTPUT_EXTENSION}"
        )

    @staticmethod
    def build_output_path(file_path: str | Path) -> Path:
        """
        Returns the full output file path.

        Output files are written to the project's
        configured output directory.
        """

        FileService.create_directory(OUTPUT_DIR)

        return OUTPUT_DIR / FileService.build_output_filename(file_path)

    @staticmethod
    def is_output_file(file_path: str | Path) -> bool:
        """
        Determines whether the supplied file already appears
        to be a cleaned output file.
        """

        return Path(file_path).stem.endswith(OUTPUT_FILE_SUFFIX)

    @staticmethod
    def resolve(file_path: str | Path) -> Path:
        """
        Returns the absolute resolved path.
        """

        return Path(file_path).expanduser().resolve()


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - FileService
#
# Public Methods
# - file_exists()
# - directory_exists()
# - create_directory()
# - is_supported_file()
# - get_file_name()
# - get_file_stem()
# - get_file_extension()
# - get_parent_directory()
# - build_output_filename()
# - build_output_path()
# - is_output_file()
# - resolve()
#
# Dependencies
# - pathlib
# - src.config