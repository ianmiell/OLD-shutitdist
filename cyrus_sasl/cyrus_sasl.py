"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class cyrus_sasl(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
#TODO http://www.linuxfromscratch.org/blfs/view/svn/postlfs/cyrus-sasl.html
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
	return cyrus_sasl(
		'shutit.tk.sd.cyrus_sasl.cyrus_sasl', 158844782.9001295817285,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.setup.setup']
	)

