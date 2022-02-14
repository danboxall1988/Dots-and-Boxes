class Foo:
	@staticmethod
	def static():
		Foo.t(Foo)
		
	def t(self):
		print(True)
	

		
foo = Foo()
Foo.static()	
		
