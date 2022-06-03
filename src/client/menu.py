
class MenuItem:
    def __init__(self, keypress: str, title: str) -> None:
        self.keypress = keypress
        self.title = title

class ForumMenuItem(MenuItem):
    def __init__(self, keypress: str, title: str, timestamp: int = 0, subheading: str = '') -> None:
        super().__init__(keypress, title)
        self.subheading = subheading
        self.timestamp = timestamp

class SubMenuMenuItem(MenuItem):
    pass

class Menu:
    def __init__(self) -> None:
        self.items = {}

    def append(self, item: MenuItem):
        self.items[item.keypress] = item


