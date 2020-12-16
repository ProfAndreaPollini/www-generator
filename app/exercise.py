
from typing import List
from app.core import WebPage

class Exercise(WebPage):
	def __init__(self) -> None:
		super().__init__()
		self.question = ""
		self.answer = ""
		self.kind = "exercise"
		self.title = "esercizio 1"
		self.section = "esercizio"
		self.subjects: List[str] = []


	def render(self, env):
		template = env.get_template('exercise.md')
		content = template.render(obj=self)
		self.add(content)
		return super().render(env)


class ProgrammingExercise(Exercise):

	def __init__(self) -> None:
		super().__init__()
		self.programming_language = ""

	def render(self, env):
		template = env.get_template('programming_exercise.md')
		content = template.render(obj=self)
		self.add(content)
		return super().render(env)