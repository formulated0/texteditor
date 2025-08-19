from textual.app import App, ComposeResult
from textual.widgets import Footer
from textual.containers import Container
from .widgets import Sidebar, Editorpane, Tabbar


class tedit(App):
    BINDINGS = [("q", "quit", "Quit")]
    CSS_PATH = "../style.tcss"
    
    def compose(self) -> ComposeResult:
        yield Sidebar()
        yield Container(
            Tabbar(),
            Editorpane(),
            classes="right-panel"
        )
        yield Footer()

