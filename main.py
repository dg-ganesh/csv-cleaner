"""
Project : CSV Cleaner
Project ID : 008

Application Entry Point
"""

from src.ui.callbacks import Callbacks
from src.ui.event_handlers import EventHandlers
from src.ui.layout_manager import LayoutManager
from src.ui.main_window import MainWindow
from src.ui.widget_factory import WidgetFactory


def main() -> None:
    """
    Creates and starts the application.
    """

    # Create main application window
    window = MainWindow()

    root = window.get_root()

    # Create UI widgets
    widgets = WidgetFactory(root)

    # Arrange widgets
    layout = LayoutManager(widgets)
    layout.arrange()

    # Register callbacks
    callbacks = Callbacks(widgets)

    # Register UI events
    events = EventHandlers(
        widgets,
        callbacks
    )

    events.register()

    # Start application
    window.start()


if __name__ == "__main__":
    main()


# =============================================================================
# Public Interface
# =============================================================================

# Public Functions
# - main()
#
# Dependencies
# - src.ui.main_window
# - src.ui.widget_factory
# - src.ui.layout_manager
# - src.ui.callbacks
# - src.ui.event_handlers