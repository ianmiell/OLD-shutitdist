"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class python_pip(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('curl https://bootstrap.pypa.io/get-pip.py | python')
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
	return python_pip(
		'shutit.tk.sd.python_pip.python_pip', 158844782.0068,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.python2.python2','shutit.tk.sd.zlib.zlib']
	)

