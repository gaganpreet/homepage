import json
from jinja2 import FileSystemLoader
from jinja2.environment import Environment

env = Environment()
env.loader = FileSystemLoader('./templates')

def index():
    template = env.get_template('index.html')
    sites = json.load(open('sites.json'))
    html = template.render(sites=sites, title="Home")
        
    output = open('index.html', 'w')
    output.write(html)

def projects():
    template = env.get_template('projects.html')
    html = template.render(title = 'Projects')

    output = open('projects.html', 'w')
    output.write(html)

def make_404():
    template = env.get_template('404.html')
    html = template.render(title = 'Page not found')

    output = open('404.html', 'w')
    output.write(html)
    
pages = [index, projects, make_404]

if __name__ == '__main__':
    for page in pages:
        page()
