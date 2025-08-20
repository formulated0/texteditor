from textual.widgets import DirectoryTree
from argparse import ArgumentParser
from pathlib import Path

class Sidebar(DirectoryTree):
    def __init__(self, folder):
        super().__init__("", classes="sidebar")
        self.folder = folder
        self.file = None
    
    def _on_director_tree_file_selected(self, event):
        path: Path = event.path
        if not path.is_file:
            return

        self.file = path

        texteditor = self.query_one(".editorpane")

        # i dont know why this doesnt work but nothing seems broken so leave it 
        texteditor.text = self.file.read_text()
        texteditor.language = "python" if self.file.suffix == "py" else None
