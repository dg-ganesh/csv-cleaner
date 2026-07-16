"""
Project : CSV Cleaner
Project ID : 008

Main Window
"""

import tkinter as tk

from src.config import (
    WINDOW_HEIGHT,
    WINDOW_RESIZABLE,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)


class MainWindow:
    """
    Creates and manages the application's main window.

    This module is responsible only for window creation
    and application startup.
    """

    def __init__(self) -> None:
        """
        Initializes the application window.
        """

        self.root = tk.Tk()

        self._configure_window()

    def _configure_window(self) -> None:
        """
        Configures the main application window.
        """

        self.root.title(WINDOW_TITLE)

        self.root.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
        )

        self.root.resizable(
            WINDOW_RESIZABLE,
            WINDOW_RESIZABLE
        )

    def get_root(self) -> tk.Tk:
        """
        Returns the Tk root window.
        """

        return self.root

    def start(self) -> None:
        """
        Starts the application.
        """

        self.root.mainloop()


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - MainWindow
#
# Public Methods
# - get_root()
# - start()
#
# Dependencies
# - tkinter
# - src.config