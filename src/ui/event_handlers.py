"""
Project : CSV Cleaner
Project ID : 008

Event Handlers
"""

from src.ui.callbacks import Callbacks
from src.ui.widget_factory import WidgetFactory


class EventHandlers:
    """
    Registers all UI event handlers.

    This module is responsible only for connecting
    widgets to callback methods.
    """

    def __init__(
        self,
        widgets: WidgetFactory,
        callbacks: Callbacks
    ) -> None:

        self.widgets = widgets
        self.callbacks = callbacks

    def register(self) -> None:
        """
        Registers all application events.
        """

        self.widgets.btn_browse.configure(
            command=self.callbacks.browse_csv
        )

        self.widgets.btn_clean.configure(
            command=self.callbacks.clean_csv
        )


# =============================================================================
# Public Interface
# =============================================================================

# Public Class
# - EventHandlers
#
# Public Methods
# - register()
#
# Dependencies
# - src.ui.callbacks
# - src.ui.widget_factory