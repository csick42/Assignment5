import DAL


def test_projects_page_empty(client, temp_db_path):
    rv = client.get('/projects')
    assert rv.status_code == 200
    # Should render projects page even if empty
    assert b'Projects' in rv.data or b'projects' in rv.data


def test_add_project_flow(client, temp_db_path):
    # POST to add a project
    data = {
        'title': 'Web Test',
        'description': 'Testing via client',
        'image_filename': 'img.png'
    }
    rv = client.post('/add_project', data=data, follow_redirects=True)
    # After successful add, should redirect to thank you or show thankyou page
    assert rv.status_code == 200
    assert b'Thank' in rv.data or b'thank' in rv.data

    # Confirm project appears in /projects
    rv2 = client.get('/projects')
    assert b'Web Test' in rv2.data


def test_project_detail_redirect_for_missing(client, temp_db_path):
    # Access a project that doesn't exist should redirect to projects
    rv = client.get('/project/9999', follow_redirects=True)
    assert rv.status_code == 200
    # Should end up on projects page
    assert b'Projects' in rv.data or b'projects' in rv.data
