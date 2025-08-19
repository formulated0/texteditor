from textual.widgets import Static

class Tabbar(Static):
    def __init__(self) -> None:
        super().__init__("placeholder tab bar", classes="tabbar")
