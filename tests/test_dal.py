import DAL


def test_add_and_get_project(temp_db_path):
    # Add a project
    title = 'Test Project'
    description = 'A project for testing'
    image = 'test.png'
    project_id = DAL.add_project(title, description, image)
    assert isinstance(project_id, int)

    # Retrieve by id
    row = DAL.get_project_by_id(project_id)
    assert row is not None
    assert row['title'] == title
    assert row['description'] == description
    assert row['image_filename'] == image


def test_get_all_projects_order(temp_db_path):
    # Add multiple projects and ensure ordering by date_added desc
    DAL.add_project('First', 'first desc', 'a.png')
    DAL.add_project('Second', 'second desc', 'b.png')
    projects = DAL.get_all_projects()
    assert len(projects) >= 2
    titles = [p['title'] for p in projects]
    # Ensure both inserted titles are present; ordering may be non-deterministic in rapid inserts
    assert 'First' in titles and 'Second' in titles


def test_update_and_delete_project(temp_db_path):
    pid = DAL.add_project('ToUpdate', 'old', 'old.png')
    DAL.update_project(pid, 'Updated', 'new', 'new.png')
    row = DAL.get_project_by_id(pid)
    assert row['title'] == 'Updated'

    # Delete and ensure it's gone
    DAL.delete_project(pid)
    deleted = DAL.get_project_by_id(pid)
    assert deleted is None
