import os
import tempfile
import pytest
from app import app as flask_app
import DAL

@pytest.fixture(scope='function')
def temp_db_path(tmp_path, monkeypatch):
    """Create a temporary sqlite database file and point DAL to it via env var"""
    db_file = tmp_path / "test_projects.db"
    # Ensure env var used by DAL
    monkeypatch.setenv('PROJECTS_DB', str(db_file))
    # Re-import or reconfigure DAL's DATABASE_NAME if necessary
    # Update the module variable
    DAL.DATABASE_NAME = str(db_file)
    # Initialize schema
    DAL.init_db()
    yield str(db_file)
    # cleanup handled by tmp_path

@pytest.fixture(scope='function')
def client(temp_db_path):
    """Flask test client with temp DB"""
    flask_app.config['TESTING'] = True
    # Ensure app imports use the monkeypatched DAL settings
    with flask_app.test_client() as client:
        yield client
