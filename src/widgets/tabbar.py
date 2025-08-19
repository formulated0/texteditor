from textual.widgets import Static, Tabs

class Tabbar(Static):
    def __init__(self) -> None:
        super().__init__("placeholder tab bar", classes="tabbar")