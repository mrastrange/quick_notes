# 📝 Quick Notes

## 1. Project Description
Quick Notes is a command-line based note management tool built in Python. It allows users to easily add, view, and manage notes, with all data stored locally in a CSV file. The codebase follows clean architecture principles and utilizes common design patterns like Command and Observer.



## 2. Features
1. **Add Notes** – Create and save notes via CLI.
2. **View Notes** – List all saved notes in a readable format.
3. **Delete Notes** – Remove specific notes by ID.
4. **Modular Structure** – Uses design patterns like Command, Observer, and State.
5. **Local CSV Storage** – Notes are saved in `notes.csv`.
6. **Vercel Compatible** – Includes `vercel.json` for optional deployment.



## 3. Project Structure

```
quick_notes/
├── app.py              # Main application launcher
├── note.py             # Note object and logic
├── command.py          # CLI command parser and executor
├── state.py            # App state management
├── decorators.py       # Utility decorators
├── notes.csv           # Stores user notes
├── requirements.txt    # Python dependencies
├── vercel.json         # Optional Vercel deployment config
└── readme.md           # Documentation
```

## 4. Setup and Installation

### Prerequisites
- Python 3.x

### Steps

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/quick_notes.git
cd quick_notes
```
2. **(Optional) Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
4. **Run the app**
```bash
python app.py
```

## 5. Design Patterns Used

1.**Command Pattern** – Wraps user actions into command objects.
2.**Observer Pattern** – Monitors state changes for side-effects.
3.**State Pattern** – Dynamically alters app behavior based on internal state.

## License
This project is open-source and available under the [MIT License](LICENSE)
