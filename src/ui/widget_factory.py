"""
Project : CSV Cleaner
Project ID : 008

Widget Factory
"""

import tkinter as tk
from tkinter import ttk

from src.config import (
    BROWSE_BUTTON_TEXT,
    CLEAN_BUTTON_TEXT,
    DEFAULT_REPLACEMENT_VALUE,
    STATUS_READY,
    TEXT_CASE_OPTIONS,
)


class WidgetFactory:
    """
    Creates all widgets required by the application.

    This module is responsible only for widget creation.
    It performs no layout or event handling.
    """

    def __init__(self, parent: tk.Tk) -> None:

        self.parent = parent

        self.csv_file_var = tk.StringVar()

        self.replacement_value_var = tk.StringVar(
            value=DEFAULT_REPLACEMENT_VALUE
        )

        self.text_case_var = tk.StringVar(
            value=TEXT_CASE_OPTIONS[2]
        )

        self.status_var = tk.StringVar(
            value=STATUS_READY
        )

        self.remove_duplicates_var = tk.BooleanVar()

        self.remove_empty_rows_var = tk.BooleanVar()

        self.remove_empty_columns_var = tk.BooleanVar()

        self.trim_whitespace_var = tk.BooleanVar()

        self.compress_spaces_var = tk.BooleanVar()

        self.replace_missing_values_var = tk.BooleanVar()

        self.standardize_text_var = tk.BooleanVar()

        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Creates all widgets.
        """

        self.lbl_csv_file = ttk.Label(
            self.parent,
            text="CSV File"
        )

        self.txt_csv_file = ttk.Entry(
            self.parent,
            textvariable=self.csv_file_var,
            width=60
        )

        self.btn_browse = ttk.Button(
            self.parent,
            text=BROWSE_BUTTON_TEXT
        )

        self.frm_options = ttk.LabelFrame(
            self.parent,
            text="Cleaning Options"
        )

        self.chk_remove_duplicates = ttk.Checkbutton(
            self.frm_options,
            text="Remove Duplicate Rows",
            variable=self.remove_duplicates_var
        )

        self.chk_remove_empty_rows = ttk.Checkbutton(
            self.frm_options,
            text="Remove Empty Rows",
            variable=self.remove_empty_rows_var
        )

        self.chk_remove_empty_columns = ttk.Checkbutton(
            self.frm_options,
            text="Remove Empty Columns",
            variable=self.remove_empty_columns_var
        )

        self.chk_trim_whitespace = ttk.Checkbutton(
            self.frm_options,
            text="Trim Whitespace",
            variable=self.trim_whitespace_var
        )

        self.chk_compress_spaces = ttk.Checkbutton(
            self.frm_options,
            text="Compress Multiple Spaces",
            variable=self.compress_spaces_var
        )

        self.chk_replace_missing = ttk.Checkbutton(
            self.frm_options,
            text="Replace Missing Values",
            variable=self.replace_missing_values_var
        )

        self.lbl_replacement = ttk.Label(
            self.frm_options,
            text="Replacement Value"
        )

        self.txt_replacement = ttk.Entry(
            self.frm_options,
            textvariable=self.replacement_value_var,
            width=20
        )

        self.chk_standardize = ttk.Checkbutton(
            self.frm_options,
            text="Standardize Text Case",
            variable=self.standardize_text_var
        )

        self.cbo_text_case = ttk.Combobox(
            self.frm_options,
            textvariable=self.text_case_var,
            values=TEXT_CASE_OPTIONS,
            state="readonly",
            width=12
        )

        self.btn_clean = ttk.Button(
            self.parent,
            text=CLEAN_BUTTON_TEXT
        )

        self.lbl_status_title = ttk.Label(
            self.parent,
            text="Status"
        )

        self.lbl_status = ttk.Label(
            self.parent,
            textvariable=self.status_var
        )


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - WidgetFactory
#
# Public Methods
# - create_widgets()
#
# Dependencies
# - tkinter
# - tkinter.ttk
# - src.config