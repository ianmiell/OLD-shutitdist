"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class bison(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/bison')
		shutit.send('cd /tmp/build/bison')
		version = shutit.cfg[self.module_id]['version']
		shutit.send('curl -L http://ftp.gnu.org/gnu/bison/bison-' + version + '.tar.gz | tar -zxf -')
		shutit.send('cd bison*' + version)
		shutit.send('./configure --prefix=/usr --with-libiconv-prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id, 'version', '3.0')
		return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		#shutit.send('rm -rf
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return bison(
		'shutit.tk.sd.bison.bison', 158844782.0039,
		description='Bison compilation',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.pkg_config.pkg_config']
	)

