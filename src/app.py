from textual.app import App, ComposeResult
from textual.widgets import Footer
from textual.containers import Container
from .widgets import Sidebar, Editorpane, Tabbar, Statusbar


class tedit(App):
    BINDINGS = [
        ("ctrl+q", "quit", "quit"),
        ("ctrl+s", "save_file"),
        ("ctrl+shift+z", "redo"), # TODO: figure this out later
        ("ctrl+t", "new_tab"),
        ("ctrl+w", "close_tab")
    ]
    
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

    def action_save_file(self) -> None:
        sidebar = self.query_one(Sidebar)
        if sidebar:
            sidebar.action_save_file()
        else:
            print("error saving file i dont know why but there was an error")

