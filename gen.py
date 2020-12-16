

import os, os.path


from app.export import Exporter
from app.graph import PageRepository
from app.core import Page, SectionComponent
from app.generate import FolderGenerator
from jinja2 import Environment, PackageLoader, select_autoescape

import importlib


# print(p.as_dict())
# template = env.get_template('page.md')
# d = p.as_dict()
# print(template.render(page=d['header'], content= d['content'], blocks = d['blocks']))
	


#print(PageRepository.get_pages())

base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"output")

env = Environment(
    loader=PackageLoader('app','templates'),
    #autoescape=select_autoescape(['html', 'md'])
)


#importlib.import_module("data")
cwd= os.path.dirname(os.path.abspath(__file__))
paths = [
    os.path.join(cwd,"..",'esercizi-programmazione'),
    #os.path.join(cwd,'www-data') 
]

f = FolderGenerator(paths)
f.generate()


exporter = Exporter(env,base_path)
exporter.render_pages()


