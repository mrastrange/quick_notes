from datetime import datetime
from state import ViewState, EditState

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.last_modified = datetime.now()  # Initialize with current timestamp
        self.state = ViewState(self)  # Set the initial state to ViewState

    def __str__(self):
        # This will display the note's title, content, and last modified time
        return f"Title: {self.title}, Content: {self.content}, Last Modified: {self.last_modified.strftime('%Y-%m-%d %H:%M:%S')}"

    def __repr__(self):
        return f"Note(title={self.title}, content={self.content}, last_modified={self.last_modified})"

    def set_state(self, state):
        self.state = state

    def view(self):
        # Call view() based on the current state
        last_modified_str = self.last_modified.strftime('%Y-%m-%d %H:%M:%S')
        return {'title': self.title, 'content': self.content, 'last_modified': last_modified_str}

    def edit(self, new_title, new_content):
        # Update the title, content, and last modified time
        self.state.edit(new_title, new_content)
        self.last_modified = datetime.now()  # Update timestamp on edit
