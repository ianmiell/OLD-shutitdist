"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class setup(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.install('build-essential')
		shutit.install('curl')
		shutit.install('libcurl4-openssl-dev')
		shutit.install('m4') # do we need this?
		shutit.install('strace') # remove later, for debug
		shutit.install('vim') # remove later, for debug
		shutit.install('xterm') # remove later, for debug (resize)
		shutit.send('echo "ShutIt Distro version 0.1" > /etc/issue')
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
	return setup(
		'shutit.tk.sd.setup.setup', 158844782.0001,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)

