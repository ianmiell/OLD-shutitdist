"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class autoconf(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/autoconf')
		shutit.send('cd /tmp/build/autoconf')
		shutit.send('curl http://ftp.gnu.org/gnu/autoconf/autoconf-latest.tar.xz | xz -d | tar -xf -')
		shutit.send('cd autoconf-*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/autoconf')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return autoconf(
		'shutit.tk.sd.autoconf.autoconf', 158844782.0100925156,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.setup.setup']
	)

