"""
Project : CSV Cleaner
Project ID : 008

Processing Summary
"""

from src.models.processing_result import ProcessingResult


class ProcessingSummary:
    """
    Generates a human-readable processing summary.

    This module is responsible only for formatting
    processing results for display.
    """

    @staticmethod
    def build(
        result: ProcessingResult
    ) -> str:
        """
        Builds the processing summary.

        Args:
            result:
                Processing statistics.

        Returns:
            Multi-line summary string.
        """

        lines = [
            "CSV Cleaning Summary",
            "-" * 40,
            f"Rows Scanned              : {result.rows_scanned}",
            f"Rows Processed            : {result.rows_processed}",
            "",
            f"Duplicate Rows Removed    : {result.duplicate_rows_removed}",
            f"Empty Rows Removed        : {result.empty_rows_removed}",
            f"Empty Columns Removed     : {result.empty_columns_removed}",
            f"Spaces Trimmed            : {result.spaces_trimmed}",
            f"Multiple Spaces Removed   : {result.multiple_spaces_removed}",
            f"Missing Values Replaced   : {result.missing_values_replaced}",
            f"Text Values Standardized  : {result.text_values_standardized}",
            "",
            f"Status                    : {'Success' if result.success else 'Failed'}",
        ]

        if result.output_file is not None:
            lines.append(
                f"Output File               : {result.output_file}"
            )

        if result.message:
            lines.append(
                f"Message                   : {result.message}"
            )

        if result.warnings:

            lines.append("")
            lines.append("Warnings")

            for warning in result.warnings:
                lines.append(f" - {warning}")

        if result.errors:

            lines.append("")
            lines.append("Errors")

            for error in result.errors:
                lines.append(f" - {error}")

        return "\n".join(lines)

    @staticmethod
    def print(
        result: ProcessingResult
    ) -> None:
        """
        Prints the processing summary.

        Primarily intended for testing.
        """

        print(
            ProcessingSummary.build(result)
        )


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - ProcessingSummary
#
# Public Methods
# - build()
# - print()
#
# Dependencies
# - src.models.processing_result