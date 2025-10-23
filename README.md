# Flask Website with Database - Quick Start Guide

## Features Added in Assignment 7:

### Database Integration
- **DAL.py**: Data Access Layer for database operations
- **projects.db**: SQLite database with projects table
- **Database-driven Projects Page**: Projects pulled from database and displayed in HTML table
- **Add Projects Form**: Contact page converted to allow adding new projects
- **Immediate Updates**: New projects are viewable immediately on the projects page

## To Run This Website:

1. **Install Flask globally (one time):**
   ```powershell
   pip install flask
   ```
   Or install all dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

2. **Initialize the database (one time):**
   ```powershell
   python DAL.py
   ```

3. **Optional - Add sample data:**
   ```powershell
   python add_sample_data.py
   ```

4. **Run the Flask application:**
   ```powershell
   python app.py
   ```

5. **Open your browser to:**
   http://127.0.0.1:5000

## How to Use:

### Adding a New Project:
1. Navigate to the "Contact" page (which is now "Add New Project")
2. Fill in the form:
   - **Project Title**: Name of your project
   - **Project Description**: Detailed description
   - **Image Filename**: Name of the image file (e.g., `myproject.jpg`)
3. Make sure your image is in the `static/images/` folder
4. Click "Add Project"
5. Your project will be added to the database

### Viewing Projects:
1. Navigate to the "Projects" page
2. All projects from the database are displayed in an HTML table at the top
3. Each project shows:
   - Title
   - Description
   - Image (from your static/images folder)

## Project Structure:
```
Assignment7/
├── app.py              # Flask application with database routes
├── DAL.py              # Data Access Layer (database functions)
├── projects.db         # SQLite database (auto-created)
├── add_sample_data.py  # Script to add sample projects
├── requirements.txt    # Python dependencies
├── README.md           # This file
├── static/             
│   ├── css/
│   │   └── styles.css  # Updated with table styling
│   └── images/         # Place your project images here
└── templates/          
    ├── base.html
    ├── contact.html    # Now "Add Project" form
    ├── projects.html   # Now displays database projects
    ├── thankyou.html   # Updated success message
    └── ...
```

## Database Schema:

**projects table:**
- `id`: INTEGER PRIMARY KEY AUTOINCREMENT
- `title`: TEXT NOT NULL
- `description`: TEXT NOT NULL
- `image_filename`: TEXT NOT NULL
- `date_added`: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

## Dependencies:
- Flask 3.1.2 (or newer)
- SQLite3 (built into Python)
- All dependencies listed in requirements.txt

---

**Note:** You do NOT need to create or activate a virtual environment. The `.venv` folder has been removed as requested.