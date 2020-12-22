

from pathlib import PurePosixPath
from typing import Any,List
from rdflib.term import Literal
from slugify import slugify as s
from app.graph import PageRepository
from app.core import Page

slugify = lambda x: s(x,regex_pattern=r'[^-a-z0-9\+]+')

# class ExerciseSolutions:

# 	def __init__(self,exercise) -> None:
# 		super().__init__()
# 		self.exercise = exercise

# 	#def __call__(self, *args: Any, **kwds: Any) -> Any:
# #		solutions = []
# 		#for page in PageRepository.get_pages():
			
# 			#if page.kind == "solution" 

class Video(Page):
	def __init__(self,title,video_url) -> None:
		super().__init__("video", "video", title,  layout="video.md")
		self.video_url = video_url

class VideoIndex(Page):

	def __init__(self,title) -> None:
		super().__init__("video", "video_index", title,  layout="video_index.md")
		
	
	@property
	def pages_by_category(self):
		videos =  [page for page in PageRepository.get_pages() if page.kind =="video"]

		groups = dict()
		for e in videos:
			cat = e.categories
			if len(cat) == 0:
				cat=[""]
		
			for c in cat:
				if not c in  groups.keys():
					groups[c] =[]
				groups[c].append(e)
		return groups

	@property
	def category_slugs(self):
		videos = [x for x in PageRepository.get_pages() if x.kind == "video"]

		groups = dict()
		for e in videos:
			for c in e.categories:
				if not c in  groups.keys():
					groups[c] = slugify(c)
				#groups[c].append(e)
		return groups


class Playlist(Page):
	def __init__(self,title,video_url) -> None:
		super().__init__("playlist", "playlist", title,  layout="playlist.md")
		self._videos:List[Video]  = []
		self.set("videos",[])

	@property
	def videos(self):
		return self.props.get("videos")
	@videos.setter
	def videos(self, v):
		self._videos = v 


	def add_video(self,video:Video):
		self._videos.append(video)
		self.videos = self._videos

class PageKindSummary(Page):

	def __init__(self, kind,section):
		self.page_kind = kind
		super().__init__(section, "page_kind_summary", "",slug=kind,  layout="page_kind_summary.md")

	@property
	def pages_by_category(self):
		exercises = [x for x in PageRepository.get_pages() if x.kind == self.page_kind]

		groups = dict()
		for e in exercises:
			cat = e.categories
			if len(cat) == 0:
				cat=[""]
		
			for c in cat:
				if not c in  groups.keys():
					groups[c] =[]
				groups[c].append(e)
		return groups

	@property
	def languages(self):
		return list(set([x.language for x in PageRepository.get_pages() if x.kind=="soluzione"]))
		

	@property
	def category_slugs(self):
		exercises = [x for x in PageRepository.get_pages() if x.kind == self.page_kind]

		groups = dict()
		for e in exercises:
			for c in e.categories:
				if not c in  groups.keys():
					groups[c] = slugify(c)
				#groups[c].append(e)
		return groups




class ExercisesByLanguage(Page):

	def __init__(self, language,section):
		self.page_language = language
		super().__init__("esercizi", "exercises_by_language", "",slug=language,  layout="exercises_by_language.md")
		self.set("aliases",[f"esercizi-linguaggio-{self.page_language}"])

	def slug(self):
		return f"esercizi-{self.page_language}"

	@property
	def pages_by_category(self):
		exercises = [x.exercise for x in PageRepository.get_pages() if x.kind == "soluzione" and x.language == self.page_language]

		groups = dict()
		for e in exercises:
			cat = e.categories
			if len(cat) == 0:
				cat=[""]
		
			for c in cat:
				if not c in  groups.keys():
					groups[c] =[]
				groups[c].append(e)
		return groups

	@property
	def category_slugs(self):
		exercises = [x.exercise for x in PageRepository.get_pages() if x.kind == "soluzione" and x.language == self.page_language]


		groups = dict()
		for e in exercises:
			for c in e.categories:
				if not c in  groups.keys():
					groups[c] = slugify(c)
				#groups[c].append(e)
		return groups


class Category(Page):

	def __init__(self,term) -> None:
		self._term = slugify(term)
		super().__init__("category", "category", term,slug=self._term,  layout="category.md")
		self.set("term",term)
		
		pages = [x for x in PageRepository.get_pages() if term in x.categories]
		self.set("pages",pages)

	@property
	def term(self):
		return self._term

	@property
	def pages(self) -> List[Any]:
		return self.props.get("pages")

	@property 
	def pages_by_kind(self):
		ret = dict()
		kind = []
		for p in self.pages:
			kind.append(p.kind)
		kind = list(set(kind))
		for k in kind:
			ret[k] = [x for x in self.pages if x.kind == k]
			
		return ret

	

class Exercise(Page):
	
	def __init__(self,  title,series=[], categories=[], tags=[]) -> None:
		super().__init__("esercizi", "esercizio", title, series=series, categories=categories, tags=tags,  layout="exercise.md")
		self.add_block("soluzioni",lambda x: 2)

	def get_solutions(self):
		return [PageRepository.pages[str(page)] for page in PageRepository.graph.subjects(Literal("exercise"),Literal(self))]
			
	def exercises_with_same_category(self):
		ret = dict()
		exercises = [PageRepository.pages[str(page)] for page in PageRepository.graph.subjects(Literal("kind"),Literal("esercizio"))]
		for cat in self.categories:
			ret[(cat,slugify(cat))] = [x for x in exercises if cat in x.categories]
		return ret




	def get_other_exercises(self):
		return []

	@classmethod
	def test(cls):
		return 2

class Solution(Page):
	def __init__(self, exercise: Exercise,  series=[], categories=[], tags=[]) -> None:
		title = f"soluzione esercizio: {exercise.title}" 
		super().__init__("soluzioni", "soluzione", title, series=series, categories=categories, tags=tags,  layout="solution.md")
		#self.set("language",language)
		self.exercise = exercise
		self.props.set("exercise",exercise)
		self.props.set("language","")
		#self.props.set("categories",exercise.categories)

	def before_add(self):
		super().before_add()
		if self.language != "":
			self.props.set("title",f"[{self.language}] soluzione esercizio: {self.exercise.title}" )
			self.props.set("slug",str(PurePosixPath(self.section,slugify(f"{self.language}: {self.exercise.title}"))))

	@property
	def language(self):
		return self.props.get("language")

	@language.setter
	def language(self, value):
		self.props.set("language",value)
		self.props.set("title",f"[{value}] soluzione esercizio: {self.exercise.title}" )
		self.props.set("slug",str(PurePosixPath(self.section,slugify(f"{value}: {self.exercise.title}"))))
		print(f"new title { self.title}")


	
