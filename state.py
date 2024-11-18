class State:
    def view(self):
        pass

    def edit(self, new_title, new_content):
        pass

class ViewState(State):
    def __init__(self, note):
        self.note = note

    def view(self):
        # Display the note's content in view mode
        return f"Viewing Note: {self.note.title} - {self.note.content}"

    def edit(self, new_title, new_content):
        # Transition to EditState when the user wants to edit
        self.note.set_state(EditState(self.note))
        self.note.edit(new_title, new_content)

class EditState(State):
    def __init__(self, note):
        self.note = note

    def view(self):
        # This will return the content in EditState, for viewing after editing
        return f"Viewing (edited) Note: {self.note.title} - {self.note.content}"

    def edit(self, new_title, new_content):
        # Update the note's title and content in EditState
        self.note.title = new_title
        self.note.content = new_content
