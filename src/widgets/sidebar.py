from textual.widgets import Static

class Sidebar(Static):
    def __init__(self) -> None:
        super().__init__("placeholder sidebar", classes="sidebar")
