from textual.app import App
from textual.widgets import Header, Footer, Static

class Sidebar(Static):
    pass

class EditorApp(App):
    """A Textual code editor application"""
    CSS_PATH = "editor.css"
    def compose(self):
        yield Header()
        yield Sidebar()
        yield Static("This is the main editor area.", id="main-content")
        yield Footer()



if __name__ == "__main__":
    app = EditorApp()
    app.run()