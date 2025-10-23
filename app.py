from flask import Flask, render_template, request, redirect, url_for
import DAL

app = Flask(__name__)

# Initialize the database when the app starts
DAL.init_db()

@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')

@app.route('/resume')
def resume():
    """Resume page route"""
    return render_template('resume.html')

@app.route('/projects')
def projects():
    """Projects page route - displays all projects from database"""
    all_projects = DAL.get_all_projects()
    return render_template('projects.html', projects=all_projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    """Project detail page - shows full information for a single project"""
    project_row = DAL.get_project_by_id(project_id)
    if project_row is None:
        return redirect(url_for('projects'))
    # Convert sqlite3.Row to dict
    project = dict(project_row)
    # Inject links/files for each project (based on title)
    # This should match the sample_projects structure in add_sample_data.py
    if project['title'] == 'FinTime – AI-powered Financial Advisor (Honors I‑Core)':
        project['links'] = [
            {
                'label': 'Kelley Blog Write-up',
                'url': 'https://blog.kelley.indianapolis.iu.edu/2024/03/11/kelley-indianapolis-honors-students-pitch-ai-product-development-projects-to-experts/'
            },
            {
                'label': 'Final Capital Budgeting (.xlsx)',
                'url': '/static/resources/FinTime_Capital_Budgeting.xlsx'
            },
            {
                'label': 'Executive Brief (.docx)',
                'url': '/static/resources/FinTime_Executive_Brief.docx'
            },
            {
                'label': 'Final Presentation (.pptx)',
                'url': '/static/resources/FinTime_Final_Presentation.pptx'
            }
        ]
    elif project['title'] == 'The Effects of Social Media on the Health of College Students':
        project['image_filename'] = 'team-photo.jpg'
        project['links'] = [
            {
                'label': 'Team Project Website (Draft 2)',
                'url': '/static/resources/Website/Draft 2/TeamProjectWebsite.html'
            },
            {
                'label': 'Home Page (Draft 3)',
                'url': '/static/resources/Website/Draft 3/Home_Page_HTML.html'
            },
            {
                'label': 'Visualization Page (Draft 3)',
                'url': '/static/resources/Website/Draft 3/Visualization_Page_HTML.html'
            },
            {
                'label': 'Data Description Page (Draft 3)',
                'url': '/static/resources/Website/Draft 3/Data_Description_Page_HTML.html'
            }
        ]
    return render_template('project_detail.html', project=project)

@app.route('/contact')
def contact():
    """Original contact page route"""
    return render_template('contact.html')

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    """Add new project page route"""
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title')
        description = request.form.get('description')
        image_filename = request.form.get('image_filename')
        
        # Add project to database
        if title and description and image_filename:
            DAL.add_project(title, description, image_filename)
            return redirect(url_for('thankyou'))
    
    return render_template('add_project.html')

@app.route('/thankyou')
def thankyou():
    """Thank you page route"""
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)