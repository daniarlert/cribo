from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.reactive import var
from textual.widgets import Footer, Header, Static


class CriboApp(App):
    """
    An app to manage boomarks.
    """

    CSS_PATH = "style.css"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("d", "toggle_dark", "Toggle dark mode"),
        ("s", "toggle_sidebar", "Toggle sidebar"),
        ("a", "toggle_modal", "Toggle modal"),
    ]

    show_sidebar = var(False)
    show_add_modal = var(False)

    def watch_show_sidebar(self, show_sidebar: bool) -> None:
        """
        Called when `show_sidebar` is modified.
        """

        self.set_class(show_sidebar, "-show-sidebar")

    def watch_show_add_modal(self, show_add_modal: bool) -> None:
        """
        Called when `show_add_modal` is modified.
        """

        self.set_class(show_add_modal, "-show-add-modal")

    def compose(self) -> ComposeResult:
        """
        Create app widgets.
        """

        yield Header()
        yield Footer()
        yield Container(
            Vertical(Container(), id="sidebar"),
            Vertical(Container(), id="add-modal"),
            id="main",
        )

    def action_toggle_sidebar(self) -> None:
        """
        Action to toggle sidebar.
        """

        self.show_sidebar = not self.show_sidebar

    def action_toggle_modal(self) -> None:
        """
        Action to toggle modal.
        """

        self.show_add_modal = not self.show_add_modal


if __name__ == "__main__":
    app = CriboApp()
    app.run()
