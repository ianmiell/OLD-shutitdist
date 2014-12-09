"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class gmp(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
#svn://svn.debian.org/svn/debian-science/packages/gmp/trunk/
		shutit.send('mkdir -p /tmp/build/gmp')
		shutit.send('cd /tmp/build/gmp')
		shutit.send('curl -L https://gmplib.org/download/gmp/gmp-6.0.0a.tar.xz | xz -d | tar -xf -')
		shutit.send('cd gmp-6.0.0/')
		shutit.send('./configure --prefix=/usr --enable-cxx')
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
	return gmp(
		'shutit.tk.sd.gmp.gmp', 158844782.0013,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.pkg_config.pkg_config']
	)

