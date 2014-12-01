"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class docbookxsl(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	#def finalize(self, shutit):
	#	return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return docbookxsl(
		'shutit.tk.sd.docbookxsl.docbookxsl', 158844782.0112351235,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)

