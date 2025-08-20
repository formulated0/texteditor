from textual.widgets import DirectoryTree, TextArea
from argparse import ArgumentParser
from pathlib import Path

class Sidebar(DirectoryTree):
    def __init__(self, folder):
        super().__init__("", classes="sidebar")
        self.folder = folder
        self.file = None
    
    def _on_directory_tree_file_selected(self, event):
        path: Path = event.path
        if not path.is_file:
            return

        self.file = path

        texteditor = self.app.query_one("#editorpane", TextArea)
        
        # i dont know why this doesnt work 
        texteditor.text = self.file.read_text()
        texteditor.language = "python" if self.file.suffix == "py" else None
