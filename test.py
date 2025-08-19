from textual.app import App
from textual.widgets import Header, Footer

class EditorApp(App):
    """A Textual code editor application"""
    def compose(self):
        yield Header()
        yield Footer()


if __name__ == "__main__":
    app = EditorApp()
    app.run()