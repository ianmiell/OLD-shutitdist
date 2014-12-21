"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class shellcheck(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('cabal install shellcheck')
		shutit.send('cp /root/.cabal/bin/shellcheck /usr/bin/shellcheck')
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
	return shellcheck(
		'shutit.tk.sd.shellcheck.shellcheck', 158844782.0152,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.cabal.cabal']
	)

