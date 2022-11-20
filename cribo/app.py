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
    ]

    show_sidebar = var(True)

    def watch_show_sidebar(self, show_sidebar: bool) -> None:
        """
        Called when `show_sidebar` is modified.
        """

        self.set_class(show_sidebar, "-show-sidebar")

    def compose(self) -> ComposeResult:
        """
        Create app widgets.
        """

        yield Header()
        yield Footer()
        yield Container(
            Vertical(Container(), id="sidebar"),
            Vertical(
                Static(id="main", expand=True),
                id="main-view",
            ),
        )

    def action_toggle_sidebar(self) -> None:
        """
        Action to toggle sidebar.
        """

        self.show_sidebar = not self.show_sidebar


if __name__ == "__main__":
    app = CriboApp()
    app.run()
