from textual.app import App, ComposeResult
from textual.widgets import Footer
from textual.containers import Container
from .widgets import Sidebar, Editorpane, Tabbar, Statusbar


class tedit(App):
    BINDINGS = [("ctrl-q", "quit", "quit")]
    CSS_PATH = "../style.tcss"
    
    def __init__(self, folder):
        super().__init__()
        self.folder = folder
        self.file = None
    
    def compose(self) -> ComposeResult:
        yield Sidebar(self.folder)
        yield Container(
            Tabbar(),
            Editorpane(),
            classes="right-panel"
        )
        yield Statusbar()
        # yield Footer() # conflicts with statusbar right now

