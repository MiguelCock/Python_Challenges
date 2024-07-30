class Tree:

	def __init__(self, branch):
		self.branch = branch
		self.ramas = []

	#======================
	def add(self, branch, leaf):
		
		if self.branch == branch:
			self.ramas.append(Tree(leaf))
		elif len(self.ramas) != 0:
			for rama in self.ramas:
				rama.add(branch, leaf)

	#======================
	def res(self):
		pass


#===========main===========
tries = int(input())
for i in range(tries):
	amount = int(input())
	tree = Tree(1)
	for branch in range(amount - 1):
		branch, leaf = map(int, input().split())
		tree.add(branch, leaf)
