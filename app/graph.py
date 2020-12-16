from typing import Any, Dict, List
from app.core import Page
from rdflib import Graph, URIRef, Literal, BNode, RDF





class PageRepository:

	pages: Dict[str,Any] = {}
	graph = Graph()

	
	@classmethod
	def add(cls,page: Any):
		page.before_add()
		cls.pages[page.oid] = page
		page_ref = URIRef(page.oid)
		print(f"adding {page.slug()} - {page.oid}")
		for k,v in page.props.as_dict().items():
			#cls.graph.add((page_ref,RDF.type,Literal(page.kind)))
			cls.graph.add((page_ref,Literal(k),Literal(v)))

		

	@classmethod
	def get_pages(cls):
		return [v for k,v in cls.pages.items()]



	