from textual.widgets import DirectoryTree, TextArea
from argparse import ArgumentParser
from pathlib import Path
from .language_map import get_language_from_extension

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
		texteditor.text = self.file.read_text()
		texteditor.language = get_language_from_extension(self.file.suffix)

	def action_save_file(self, event=None):
		if event is not None:
				path: Path = event.path

				if not path.is_file:
					print("save failed because the path is not a file")
					return
				
				self.file = path

		if self.file is None:
				print("save failed because there was no file selected")
				return
		
		texteditor = self.app.query_one("#editorpane", TextArea)
		if texteditor is None:
				print("save failed because the editorpane wasnt found for some reason")
				return
		
		self.file.write_text(texteditor.text)
		print(f"saved file {self.file}")
