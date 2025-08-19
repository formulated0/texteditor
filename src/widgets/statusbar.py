from textual.widgets import Static

class Statusbar(Static):
    def __init__(self) -> None:
        super().__init__("placeholder statusbar", classes="statusbar")
