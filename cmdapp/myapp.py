from cmdapp import CommandLineApplication

class MyApp(CommandLineApplication):
	"""
	Some description.
	"""

	def __init__(self, *args, **kwargs):

		print(self.__class__.__module__)
		super().__init__(self, *args, **kwargs)
		print(self.__dict__)

if __name__ == "__main__":

	MyApp()