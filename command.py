from note import Note  # Import the Note class

class Command:
    def execute(self):
        pass

    def undo(self):
        pass

class AddNoteCommand(Command):
    def __init__(self, notes, title, content):
        self.notes = notes
        self.title = title
        self.content = content

    def execute(self):
        self.note = Note(self.title, self.content)
        self.notes.append(self.note)

    def undo(self):
        if self.note in self.notes:
            self.notes.remove(self.note)

class EditNoteCommand:
    def __init__(self, note, new_title, new_content):
        self.note = note
        self.new_title = new_title
        self.new_content = new_content
        self.prev_title = note.title
        self.prev_content = note.content

    def execute(self):
        # Call edit on the note, which will also update the last_modified timestamp
        self.note.edit(self.new_title, self.new_content)

    def undo(self):
        # Revert to the previous state
        self.note.edit(self.prev_title, self.prev_content)

class DeleteNoteCommand(Command):
    def __init__(self, notes, note):
        self.notes = notes
        self.note = note

    def execute(self):
        self.notes.remove(self.note)

    def undo(self):
        self.notes.append(self.note)

class UndoRedoManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.history = []  # Stack to store executed commands
            cls._instance.redo_stack = []  # Stack to store undone commands
        return cls._instance

    def execute(self, command):
        command.execute()
        self.history.append(command)
        self.redo_stack.clear()

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
            self.redo_stack.append(command)

    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.history.append(command)

