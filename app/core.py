from genericpath import exists
import os
from pathlib import PurePosixPath
from typing import Any, Dict, List
import datetime
import uuid


from slugify import slugify as s

slugify = lambda x: s(x,regex_pattern=r'[^-a-z0-9\+]+')

class MetaComponent(type):
	def __new__(metacls, cls, bases, attrs):
		print(attrs)
		
		if "__props__" in attrs.keys():
			props = attrs.get('__props__')
			for prop in props:
				def get(self):
					return self.props.get(prop)
				def set(self,value):
					self.props.set(prop,value)
				bases['props'] = Props()
				attrs[prop] = property(set,get)
				bases['props'].set(prop,"")
				print(dir(metacls))
		return super().__new__(metacls, cls, bases, attrs)



class GraphObject:

	def __init__(self):
		self.properties = {}

	def add_property(self,name,value):
		self.properties[name] = value

	def add_to_graph(self, g):
		"""
		docstring
		"""
		raise NotImplementedError

class WebPageComponent:

	def __init__(self) -> None:
		super().__init__()
		self.content: List[Any] = []

	def add_content(self,content_obj):
		self.content.append(content_obj)

	

	def get_graph_objects(self) -> List[Any]:
		ret = []
		for o in self.content:
			if issubclass(type(o),WebPageComponent):
				ret.extend(o.get_graph_objects())
		return ret

	def get_content(self) -> str:
		return "\n".join([str(x) for x in self.content])


class WebPage(GraphObject):

	def __init__(self):
		super().__init__()
		self.title = ""
		self.lastModified = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
		self.description = ""
		self.author = "prof. Andrea Pollini"
		self.content = []
		self.section = "page"

	def add(self,element):
		self.content.append(element)

	def render(self, env):
		template = env.get_template('web_page.md')
		return template.render(content = "".join([str(x) for x in self.content]),page=self)


		

class TextWebComponent(WebPageComponent):

	def __init__(self) -> None:
		super().__init__()
		

	def get_graph_objects(self) -> List[Any]:

		return super().get_graph_objects()

	def __repr__(self):
		return "\n".join([str(x) for x in self.content])



class Image(WebPageComponent):

	def __init__(self,imageUrl) -> None:
		super().__init__()
		self.caption = ""
		self.url = imageUrl
		self.description=""

	def __repr__(self) -> str:
		return """{{<img src="" />}}"""

class Video(WebPageComponent):

	def __init__(self,videoUrl) -> None:
		super().__init__()
		self.caption = ""
		self.url = videoUrl
		self.description=""
		self.uploadDate =  datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
		#self.embedUrl = ""

	def with_caption(self,caption):
		self.caption = caption
		return self

	def __repr__(self) -> str:
		return """{{<video src="%s" />}}""" %(self.url)

class GraphObjectComposableWeb(GraphObject):

	def __init__(self):
		super().__init__(self)
		self.components = []

	def add_component(self,component):
		self.components.append(component)



class ObjectProperties:

	def __init__(self) -> None:
		super().__init__()
		
	def __setattr__(self, name: str, value: Any) -> None:
	
		return super().__setattr__(name, value)
	
class ObjectWriter:

	def __init__(self,base_path) -> None:
		print(base_path)
		self.base = base_path

	def write(self, obj,env):
		content = obj.render(env)
		##print("content: ",content,obj.__class__.section)
		obj_path = os.path.join(self.base,obj.section,slugify(obj.title))
		if not os.path.exists(obj_path):
			os.makedirs(obj_path)
		with open(os.path.join(obj_path,"index.md"),"w+") as f:
			f.write(content)
		
class Props:

	def __init__(self) -> None:
		#super().__init__()
		self.props: List[str] = []

	def set(self, name, value):
		if not name in self.props: 
			self.props.append(name)
		setattr(self,name,value)

	def get(self,name):
		if not name in self.props: 
			return None
		return getattr(self,name)

	def as_dict(self):
		return { p:getattr(self,p) for p in self.props }



class Component():

	def __init__(self) -> None:
		super().__init__()
		self.components: List[Component] = []
		self.props = Props()

	def add(self, component: Any) -> None:
		self.components.append(component)

	@property
	def get_content(self):
		raise NotImplementedError


class SectionComponent:

	def __init__(self,title) -> None:
		super().__init__()
		self.title = title 
		self.content= ""

	def get_content(self):
		
		return dict( title= self.title, kind="section", content=self.content)

	
class Page(Component):

	def __init__(self,section,kind,title,series=[],categories=[],tags=[], last_modified = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat(),slug = None,layout = "page.md") -> None:
		super().__init__()
		
		self.set("section",section)
		self.set("title",title)
		self.set("kind",kind)
		self.set("lastModified",last_modified)
		self.set("tags",tags)
		self.set("categories",categories)
		self.set("series",series)
		self.set("summary","")
		self.set("series",[])
		self.set("layout",layout)
		self.set("related",{})
		self.set("aliases",[])
		self.set("oid","")

		if slug is None:
			slug = title
		self.props.set("slug",slug)
		self.set("slug",str(PurePosixPath(section,slugify(slug))))
		self.blocks: Dict[str,Any] = {}

	def before_add(self):
		if self.oid == "":
			self.oid = str(uuid.uuid4())

	def add_block(self,name,block):
		self.blocks[name] = block 

	@property 
	def oid(self):
		return self.props.get("oid")

	@oid.setter
	def oid(self,v):
		self.props.set("oid",v)

	@property 
	def aliases(self):
		return self.props.get("aliases")

	@aliases.setter
	def aliases(self,v):
		self.props.set("aliases",v)

	@property 
	def related(self):
		return self.props.get("related")

	@related.setter
	def related(self,v):
		self.props.set("related",v)

	@property
	def section(self):
		return self.props.__getattribute__("section")

	@property
	def title(self):
		return self.props.__getattribute__("title")

	@property
	def layout(self):
		return self.props.__getattribute__("layout")

	@layout.setter
	def layout(self, value):
		self.set("layout",value)

	@property
	def kind(self):
		return self.props.__getattribute__("kind")


	def slug(self) -> str:
		return self.props.__getattribute__("slug")


	@property
	def summary(self) -> str:
		return self.props.__getattribute__("summary")

	@summary.setter
	def summary(self, value):
		self.set("summary",value)

	@property
	def series(self) -> str:
		return self.props.__getattribute__("series")

	@series.setter
	def series(self, value):
		self.set("series",value)

	@property
	def categories(self) -> List[str]:
		return self.props.get("categories")
	@categories.setter
	def categories(self,value):
		self.props.set("categories",value)

	@property
	def tags(self) -> List[str]:
		return self.props.get("tags")
	@tags.setter
	def tags(self,tags):
		self.props.set("tags",tags)


	def set(self,name,value):
		self.props.set(name,value)

	def get(self,name):
		self.props.get(name)

	

	def as_dict(self):
		ret ={}
		ret['header'] =  self.props.as_dict()
		ret['content'] = self.get_content()
		ret['blocks'] = self.blocks
		return ret

	def get_content(self):
		ret = [x.get_content() for x in self.components]
		return ret

	

