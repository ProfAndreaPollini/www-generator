import os,os.path
import frontmatter

from app.core import SectionComponent,Page
from app.graph import PageRepository
from app.pages import Exercise, Solution,Video

class FolderGenerator:

	def __init__(self, base_paths) -> None:
		super().__init__()
		self.base_paths = base_paths

	def generate_esercizio(self,folder):
		document_index = frontmatter.load(os.path.join(folder, "index.md"))
		print(document_index.metadata,document_index.content)

		s = SectionComponent("titolo principale")
		s.content=document_index.content
		p = Exercise("trovare il massimo di un vettore")
		for k,v in document_index.metadata.items():
			p.set(k,v)
		p.add(s)
		PageRepository.add(p)

		solutions = [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder,d))]

		print("soluzioni in ", solutions)
		for solution in solutions:
			sol_cwd = os.path.join(folder,solution)

			solution_index = frontmatter.load(os.path.join(sol_cwd,"index.md"))
			print("metadati = ",solution_index.metadata)
			content = solution_index.content.split("\n")
			out = []
			for line in content:
				if line.startswith("§"):
					filename = line.split()[1]
					line_range = []
					if len(line.split()) == 3:
						line_range = line.split()[2].split(":")
					print(line_range)
					data = []
					with open(os.path.join(sol_cwd,filename),"r") as f:
						data = f.read().split("\n")
					out.append(f"```{solution}")
					if len(line_range) > 0:
						out.extend(data[int(line_range[0]):min(int(line_range[1])+1,len(data))])
					else:
						out.extend(data)
					out.append("```")

				else:
					out.append(line)
			out="\n".join(out)

			sp1 = SectionComponent("")
			sp1.content=out

			sol = Solution(p)
			for k,v in solution_index.metadata.items():
				sol.set(k,v)
			#sol.add(s)
			sol.add(sp1)
			PageRepository.add(sol)

	def generate_video(self, folder):
		document_index = frontmatter.load(os.path.join(folder, "index.md"))
		print(document_index.metadata,document_index.content)

		s = SectionComponent("")
		s.content=document_index.content
		p = Video(document_index.metadata['title'],document_index.metadata['video'])
		for k,v in document_index.metadata.items():
			p.set(k,v)
		p.add(s)
		PageRepository.add(p)


	def generate(self):
		for b in self.base_paths:
			folders = [d for d in os.listdir(b) if os.path.isdir(os.path.join(b,d))]
			for folder in folders:
				kind = folder.split("-")[0]
				print(folder,kind)
				cwd = os.path.join(b,folder)
				try:
					getattr(self,f"generate_{kind}")(cwd)
				except:
					pass
			
