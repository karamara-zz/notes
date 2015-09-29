from system.core.controller import *

class Notes(Controller):
	def __init__(self,action):
		super(Notes,self).__init__(action)
		self.load_model('Note')
	def index(self):
		notes=self.models['Note'].get_all()
		return self.load_view('/notes/index.html',notes=notes)
	def delete(self,id):
		self.models['Note'].delete(id)
		return redirect('notes/partial')
	def add(self):
		if request.form['addTitle']:
			title=request.form['addTitle']
			self.models['Note'].add(title)
			return redirect('notes/partial')
	def update(self,id):
		print id
		content= request.form['contents']
		print content
		self.models['Note'].update(content,id)
		return redirect('notes/partial')
	def partial(self):
		notes=self.models['Note'].get_all()
		return self.load_view('/partials/partial.html', notes=notes)

