from flask import Flask, request, redirect, url_for, render_template
from decorators import BoldDecorator, ItalicDecorator, UnderlineDecorator
from note import Note
from command import AddNoteCommand, EditNoteCommand, DeleteNoteCommand, UndoRedoManager
import threading
import csv


app = Flask(__name__)
notes = []  # List to store Note objects
undo_redo_manager = UndoRedoManager()  # Initialize the UndoRedoManager

# Save notes to CSV
def save_notes():
    with open('notes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for note in notes:
            writer.writerow([note.title, note.content])

# Load notes from CSV
def load_notes():
    try:
        with open('notes.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) == 2:  # Ensure there are exactly two values (title, content)
                    title, content = row
                    note = Note(title, content)
                    notes.append(note)
    except FileNotFoundError:
        pass

# Route to display all notes
@app.route('/')
def index():
    # Render the notes' title and content using the view method
    notes_data = [note.view() for note in notes]
    return render_template('index.html', notes=notes_data)

# Route to add a new note
@app.route('/add_note', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    format_type = request.form.get('format')

    # Apply formatting if specified
    if format_type == 'bold':
        content = BoldDecorator(content).apply_format()
    elif format_type == 'italic':
        content = ItalicDecorator(content).apply_format()
    elif format_type == 'underline':
        content = UnderlineDecorator(content).apply_format()

    command = AddNoteCommand(notes, title, content)
    undo_redo_manager.execute(command)
    
    threading.Thread(target=save_notes).start()
    return redirect(url_for('index'))

# Route to handle editing or deleting a note based on form input
@app.route('/edit_delete_note/<int:note_id>', methods=['POST'])
def edit_delete_note(note_id):
    note = notes[note_id]
    action = request.form['action']

    if action == 'edit':
        # Perform the edit operation
        new_title = request.form['title']
        new_content = request.form['content']
        format_type = request.form.get('format')

        if format_type == 'bold':
            new_content = f"<b>{new_content}</b>"
        elif format_type == 'italic':
            new_content = f"<i>{new_content}</i>"
        elif format_type == 'underline':
            new_content = f"<u>{new_content}</u>"

        command = EditNoteCommand(note, new_title, new_content)
        undo_redo_manager.execute(command)

    elif action == 'delete':
        # Perform the delete operation
        command = DeleteNoteCommand(notes, note)
        undo_redo_manager.execute(command)

    threading.Thread(target=save_notes).start()
    return redirect(url_for('index'))

# Initialize the app with notes
load_notes()  # Load notes from CSV on startup

if __name__ == "__main__":
    app.run(debug=True)
