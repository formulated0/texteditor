from textual.widgets import TextArea

class Editorpane(TextArea):
    
    def __init__(self) -> None:
        super().__init__("placeholder editorpane", id="editorpane")