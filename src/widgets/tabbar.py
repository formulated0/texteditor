from textual.widgets import Static, Tabs

NAMES = 

class Tabbar(Static):
    def __init__(self) -> None:
        super().__init__("placeholder tab bar", classes="tabbar")
    
    def action_new_tab(self) -> None:
        tabs = self.query_one(Tabs)
        NAMES[:] = [*NAMES[1:], NAMES[0]] 
        tabs.add_tab(NAMES[0])