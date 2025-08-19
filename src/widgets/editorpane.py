from textual.widgets import Static

class Editorpane(Static):
    def __init__(self) -> None:
        super().__init__("placeholder editorpane", classes="editorpane")