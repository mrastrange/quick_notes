class TextDecorator:
    def __init__(self, content):
        self.content = content

    def apply_format(self):
        return self.content

class BoldDecorator(TextDecorator):
    def apply_format(self):
        return f"<b>{self.content}</b>"

class ItalicDecorator(TextDecorator):
    def apply_format(self):
        return f"<i>{self.content}</i>"

class UnderlineDecorator(TextDecorator):
    def apply_format(self):
        return f"<u>{self.content}</u>"
