from app.pages import Category, ExercisesByLanguage, PageKindSummary, VideoIndex
from app.graph import PageRepository
import os, os.path,io, codecs

from jinja2 import Environment, PackageLoader, select_autoescape

from slugify import slugify as s
slugify = lambda x: s(x,regex_pattern=r'[^-a-z0-9\+]+')

class Exporter:

	def __init__(self,env : Environment,base_path) -> None:
		super().__init__()
		self.base_path = os.path.join(base_path,"content")
		self.env = env

	def render_pages(self):
		#print("--- printing raw triples ---")
		#for s, p, o in PageRepository.graph:
	#		print((s, p, o))
	#	print("--- printing raw triples ---")

		categories = []
		page_kind_list = set()
		for page in PageRepository.get_pages():
			categories.extend(page.categories)
			page_kind_list.add((page.kind,page.section))
		categories = list(set(categories))
		page_kind_list = list(page_kind_list)
		print("page kind list",page_kind_list)

		for term in categories:
			term_page = Category(term)
			PageRepository.add(term_page)

		for page_kind,page_section in page_kind_list:
			p = PageKindSummary(page_kind,page_section)
			PageRepository.add(p)

		vi  =VideoIndex("Elenco Video")
		PageRepository.add(vi)

		print("linguaggi = ",[x.language for x in PageRepository.get_pages() if x.kind=="soluzione"])
		print("linguaggi = ",[slugify(x.language) for x in PageRepository.get_pages() if x.kind=="soluzione"])
		languages = list(set([x.language for x in PageRepository.get_pages() if x.kind=="soluzione"]))
		for l in languages:
			ebl = ExercisesByLanguage(l,"")
			PageRepository.add(ebl)

		for page in PageRepository.get_pages():
			print(f"rendering {page.slug()}({page.kind}) with layout {page.layout}")
			template = self.env.get_template(page.layout)
			d = page.as_dict()
			
			output = template.render(page=d['header'], content= d['content'], blocks = d['blocks'], obj=page)
			if page.section == "category":
				obj_path = os.path.join(self.base_path,page.section)
				if not os.path.exists(obj_path):
					os.makedirs(obj_path)
				with codecs.open(os.path.join(obj_path,f"{page.term}.md"),"w+",encoding='utf8') as f:
					f.write(output)
			else:
				if page.kind == "page_kind_summary":
					obj_path = os.path.join(self.base_path,page.section)
					if not os.path.exists(obj_path):
						os.makedirs(obj_path)
					with codecs.open(os.path.join(obj_path,f"_index.md"),"w+",encoding='utf8') as f:
						f.write(output)
				elif page.kind == "exercises_by_language":
					obj_path = os.path.join(self.base_path,"exercises_by_language",page.page_language)
					print(f"§§ {obj_path}")
					if not os.path.exists(obj_path):
						os.makedirs(obj_path)
					with codecs.open(os.path.join(obj_path,f"_index.md"),"w+",encoding='utf8') as f:
						f.write(output)
				elif page.kind == "video_index":
					obj_path = os.path.join(self.base_path,page.section)
					if not os.path.exists(obj_path):
						os.makedirs(obj_path)
					with codecs.open(os.path.join(obj_path,f"_index.md"),"w+",encoding='utf8') as f:
						f.write(output)
				else:
					obj_path = os.path.join(self.base_path,page.section,slugify(page.title))
					if not os.path.exists(obj_path):
						os.makedirs(obj_path)
					with codecs.open(os.path.join(obj_path,"_index.md"),"w+",encoding='utf8') as f:
						f.write(output)

