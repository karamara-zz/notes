from system.core.model import Model

class Note(Model):
	def __init__(self):
		super(Note, self).__init__()
	def get_all(self):
		get_all_query="select * from notes order by updated_at desc"
		get_all=self.db.query_db(get_all_query)
		return get_all
	def delete(self,id):
		delete_query='delete from notes where id={}'.format(id)
		self.db.query_db(delete_query)
	def add(self,title):
		add_query="insert into notes (title,updated_at,created_at) values ('{}',now(),now())".format(title)
		self.db.query_db(add_query)
	def update(self,content,id):
		update_query="update notes set content='{}', updated_at=now() where notes.id= {}".format(content,id)
		self.db.query_db(update_query)

