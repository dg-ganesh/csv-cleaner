"""
Project : CSV Cleaner
Project ID : 008

Layout Manager
"""

from tkinter import ttk

from src.ui.widget_factory import WidgetFactory


class LayoutManager:
    """
    Arranges all application widgets.

    This module is responsible only for widget layout.
    It performs no widget creation or event handling.
    """

    def __init__(
        self,
        widgets: WidgetFactory
    ) -> None:

        self.widgets = widgets

    def arrange(self) -> None:
        """
        Arranges all widgets on the window.
        """

        self._layout_file_section()
        self._layout_options_section()
        self._layout_action_section()
        self._layout_status_section()

    def _layout_file_section(self) -> None:
        """
        Arranges the file selection controls.
        """

        self.widgets.lbl_csv_file.grid(
            row=0,
            column=0,
            padx=10,
            pady=(10, 5),
            sticky="w"
        )

        self.widgets.txt_csv_file.grid(
            row=1,
            column=0,
            padx=(10, 5),
            pady=5,
            sticky="ew"
        )

        self.widgets.btn_browse.grid(
            row=1,
            column=1,
            padx=(0, 10),
            pady=5
        )

    def _layout_options_section(self) -> None:
        """
        Arranges the cleaning options.
        """

        frame = self.widgets.frm_options

        frame.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky="ew"
        )

        self.widgets.chk_remove_duplicates.grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=2
        )

        self.widgets.chk_remove_empty_rows.grid(
            row=1,
            column=0,
            sticky="w",
            padx=10,
            pady=2
        )

        self.widgets.chk_remove_empty_columns.grid(
            row=2,
            column=0,
            sticky="w",
            padx=10,
            pady=2
        )

        self.widgets.chk_trim_whitespace.grid(
            row=3,
            column=0,
            sticky="w",
            padx=10,
            pady=2
        )

        self.widgets.chk_compress_spaces.grid(
            row=4,
            column=0,
            sticky="w",
            padx=10,
            pady=2
        )

        self.widgets.chk_replace_missing.grid(
            row=5,
            column=0,
            sticky="w",
            padx=10,
            pady=2
        )

        self.widgets.lbl_replacement.grid(
            row=6,
            column=0,
            sticky="w",
            padx=10,
            pady=(8, 2)
        )

        self.widgets.txt_replacement.grid(
            row=7,
            column=0,
            padx=10,
            pady=2,
            sticky="w"
        )

        self.widgets.chk_standardize.grid(
            row=8,
            column=0,
            sticky="w",
            padx=10,
            pady=(8, 2)
        )

        self.widgets.cbo_text_case.grid(
            row=9,
            column=0,
            padx=10,
            pady=(2, 10),
            sticky="w"
        )

    def _layout_action_section(self) -> None:
        """
        Arranges action controls.
        """

        self.widgets.btn_clean.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=(0, 10)
        )

    def _layout_status_section(self) -> None:
        """
        Arranges the status controls.
        """

        self.widgets.lbl_status_title.grid(
            row=4,
            column=0,
            padx=10,
            sticky="w"
        )

        self.widgets.lbl_status.grid(
            row=5,
            column=0,
            columnspan=2,
            padx=10,
            pady=(2, 10),
            sticky="w"
        )


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - LayoutManager
#
# Public Methods
# - arrange()
#
# Dependencies
# - tkinter.ttk
# - src.ui.widget_factory