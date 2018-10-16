
from tinydb import TinyDB, Query
import random
db = TinyDB('./lessons.json')

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

COUNTRIES = ['US']
PROJECT_TYPES = ['Condo', 'Residence', 'Apartment', 'Civil', 'Commercial', 'Industrial', 'Government', 'Retail']
REPORT_LINKS = ['']
IMPORTANCES = [1,2,3]
CONSTRUCTION_TECH = [
    'Ceramics',
    'Composites',
    'Concrete',
    'Glass',
    'Steel',
    'Metals'
]
EXPERIENCE_TYPE = ['Best Practice', 'Problem']

def get_random(items):
    return random.choice(items)

with open('lessons.txt', 'r') as f:
    content = f.readlines()
    lessons = chunks(content, 2)
    for item in lessons:
        db.insert({
            'country': get_random(COUNTRIES),
            'project_type': get_random(PROJECT_TYPES),
            'title': item[0].rstrip('\n'),
            'construction_technology': get_random(CONSTRUCTION_TECH),
            'importance': get_random(IMPORTANCES),
            'experience_type': get_random(EXPERIENCE_TYPE),
            'description': item[1].rstrip('\n'),
            'report_link': get_random(REPORT_LINKS)
        })
