import sqlite3
import os

# Allow overriding the database filename via environment variable for tests
DATABASE_NAME = os.environ.get('PROJECTS_DB', 'projects.db')

def get_db_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn

def init_db():
    """Initialize the database and create the projects table if it doesn't exist"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create projects table with Title, Description, ImageFileName, and DateAdded
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            image_filename TEXT NOT NULL,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

def get_all_projects():
    """Retrieve all projects from the database"""
    conn = get_db_connection()
    projects = conn.execute('SELECT * FROM projects ORDER BY date_added DESC').fetchall()
    conn.close()
    return projects

def get_project_by_id(project_id):
    """Retrieve a single project by ID"""
    conn = get_db_connection()
    project = conn.execute('SELECT * FROM projects WHERE id = ?', (project_id,)).fetchone()
    conn.close()
    return project

def add_project(title, description, image_filename):
    """Add a new project to the database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO projects (title, description, image_filename) VALUES (?, ?, ?)',
        (title, description, image_filename)
    )
    conn.commit()
    project_id = cursor.lastrowid
    conn.close()
    return project_id

def update_project(project_id, title, description, image_filename):
    """Update an existing project"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE projects SET title = ?, description = ?, image_filename = ? WHERE id = ?',
        (title, description, image_filename, project_id)
    )
    conn.commit()
    conn.close()

def delete_project(project_id):
    """Delete a project from the database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
    conn.commit()
    conn.close()

# Initialize the database when this module is imported
if __name__ == '__main__':
    init_db()
    print("Database setup complete!")
