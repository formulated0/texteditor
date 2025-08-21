from textual.widgets import TextArea
from textual import events

class Editorpane(TextArea):	
	def __init__(self) -> None:
		super().__init__("", id="editorpane")
		self.show_line_numbers = True
		self.indent_type = "tabs"
		self.tab_behavior = "indent"

	def _on_key(self, event: events.Key) -> None:
		if event.character == "(":
			self.insert("()")
			self.move_cursor_relative(columns=-1)
			event.prevent_default()
		
		if event.character == "{":
			self.insert("{}")
			self.move_cursor_relative(columns=-1)
			event.prevent_default()
		
		if event.character == "[":
			self.insert("[]")
			self.move_cursor_relative(columns=-1)
			event.prevent_default()

		if event.character == '"':
			self.insert('""')
			self.move_cursor_relative(columns=-1)
			event.prevent_default()

		if event.character == "'":
			self.insert("''")
			self.move_cursor_relative(columns=-1)
			event.prevent_default()