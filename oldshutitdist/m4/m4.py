"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class m4(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/m4')
		shutit.send('cd /tmp/m4')
		shutit.send('curl http://ftp.gnu.org/gnu/m4/m4-latest.tar.xz | xz -d | tar -xf -')
		shutit.send('cd m4-*')
		shutit.send('')
		shutit.send('')
		shutit.send('')
		shutit.send('')
		shutit.send('')
		shutit.send('')
		shutit.send('')
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
	return m4(
		'shutit.tk.sd.m4.m4', 158844782.00,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)

