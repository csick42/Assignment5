"""
Script to add Christian's actual projects to the database
Run this once to populate the database with real project data
"""
import DAL

# Your actual projects from the website
sample_projects = [
    {
        'title': 'FinTime – AI-powered Financial Advisor (Honors I‑Core)',
        'description': "Kelley's I‑Core integrates Finance, Marketing, Operations, and Leadership in a rigorous, semester‑long program. In Fall 2023 Honors I‑Core, my team acted as entrepreneurs and created an AI‑powered financial advisor app called FinTime to deliver personalized guidance. The semester culminated in a final pitch to a panel of industry leaders and AI specialists. Featured by the Kelley Indianapolis blog.",
        'image_filename': 'cohort-photo.JPEG',
        'links': [
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
    },
    {
        'title': 'The Effects of Social Media on the Health of College Students',
        'description': 'This analysis explores relationships between social media use and mental well‑being among college students. Variables include time spent on social media, anxiety and depression levels, sleep patterns, and academic performance. The dataset originates from a research study hosted on OpenSIUC (a publicly accessible academic repository).',
        'image_filename': 'team-photo.jpg',
        'links': [
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
    }
]

def add_sample_data():
    """Add sample projects to the database"""
    print("Adding sample projects to database...")
    
    for project in sample_projects:
        project_id = DAL.add_project(
            project['title'], 
            project['description'], 
            project['image_filename']
        )
        print(f"Added project: {project['title']} (ID: {project_id})")
    
    print("\nAll sample projects added successfully!")
    print("\nCurrent projects in database:")
    projects = DAL.get_all_projects()
    for p in projects:
        print(f"  - {p['title']}")

if __name__ == '__main__':
    add_sample_data()
