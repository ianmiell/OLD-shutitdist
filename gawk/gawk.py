"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class gawk(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/gawk')
		shutit.send('cd /tmp/build/gawk')
		shutit.send('curl -L http://ftp.gnu.org/gnu/gawk/gawk-4.1.1.tar.xz | xz -d | tar -xf -')
		shutit.send('cd gawk*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
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
	return gawk(
		'shutit.tk.sd.gawk.gawk', 158844782.01111255322531353,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.setup.setup']
	)

