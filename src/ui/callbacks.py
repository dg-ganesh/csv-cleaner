"""
Project : CSV Cleaner
Project ID : 008

Callbacks
"""

from pathlib import Path
from tkinter import filedialog, messagebox

from src.core.cleaning_pipeline import CleaningPipeline
from src.core.csv_loader import CSVLoader
from src.core.csv_validator import CSVValidator
from src.core.processing_summary import ProcessingSummary
from src.models.cleaning_options import CleaningOptions
from src.models.processing_result import ProcessingResult
from src.services.csv_export_service import CSVExportService
from src.ui.widget_factory import WidgetFactory


class Callbacks:
    """
    Handles UI callbacks.

    This module connects the UI with the application's
    business logic.
    """

    def __init__(
        self,
        widgets: WidgetFactory
    ) -> None:

        self.widgets = widgets

    def browse_csv(self) -> None:
        """
        Browse for a CSV file.
        """

        filename = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")]
        )

        if filename:
            self.widgets.csv_file_var.set(filename)

    def clean_csv(self) -> None:
        """
        Executes the CSV cleaning workflow.
        """

        file_path = self.widgets.csv_file_var.get()

        errors = CSVValidator.validate(file_path)

        if errors:

            messagebox.showerror(
                "Validation Error",
                "\n".join(errors)
            )

            return

        options = self._build_cleaning_options()

        result = ProcessingResult()

        dataframe = CSVLoader.load(file_path)

        cleaned_dataframe = CleaningPipeline.execute(
            dataframe,
            options,
            result
        )

        output_file = CSVExportService.export(
            cleaned_dataframe,
            Path(file_path)
        )

        result.output_file = output_file

        summary = ProcessingSummary.build(result)

        self.widgets.status_var.set(
            "Completed"
        )

        messagebox.showinfo(
            "Processing Summary",
            summary
        )

    def _build_cleaning_options(
        self
    ) -> CleaningOptions:
        """
        Creates a CleaningOptions object
        from the current UI state.
        """

        options = CleaningOptions()

        options.remove_duplicate_rows = (
            self.widgets.remove_duplicates_var.get()
        )

        options.remove_empty_rows = (
            self.widgets.remove_empty_rows_var.get()
        )

        options.remove_empty_columns = (
            self.widgets.remove_empty_columns_var.get()
        )

        options.trim_whitespace = (
            self.widgets.trim_whitespace_var.get()
        )

        options.compress_multiple_spaces = (
            self.widgets.compress_spaces_var.get()
        )

        options.replace_missing_values = (
            self.widgets.replace_missing_values_var.get()
        )

        options.replacement_value = (
            self.widgets.replacement_value_var.get()
        )

        options.standardize_text_case = (
            self.widgets.standardize_text_var.get()
        )

        options.text_case = (
            self.widgets.text_case_var.get()
        )

        return options


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - Callbacks
#
# Public Methods
# - browse_csv()
# - clean_csv()
#
# Dependencies
# - tkinter.filedialog
# - tkinter.messagebox
# - src.core.*
# - src.models.*
# - src.services.csv_export_service
# - src.ui.widget_factory