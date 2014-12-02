"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class automake(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/automake')
		shutit.send('cd /tmp/build/automake')
		shutit.send('curl http://ftp.gnu.org/gnu/automake/automake-' + shutit.cfg[self.module_id]['version'] + '.tar.xz | xz -d | tar -xf -')
		shutit.send('cd /tmp/automake/automake-' + shutit.cfg[self.module_id]['version'])
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','1.14')
		return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/automake')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return automake(
		'shutit.tk.sd.automake.automake', 158844782.01010113251352435,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.autoconf.autoconf']
	)

