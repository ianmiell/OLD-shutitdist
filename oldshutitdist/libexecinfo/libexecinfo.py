"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libexecinfo(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):

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
	return libexecinfo(
		'shutit.tk.libexecinfo.libexecinfo', 0.012135246,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)

