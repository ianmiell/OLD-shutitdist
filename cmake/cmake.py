"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class cmake(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/cmake')
		shutit.send('cd /tmp/build/cmake')
		shutit.send('curl -L http://www.cmake.org/files/v3.0/cmake-3.0.1.tar.gz | tar -zxf -')
		shutit.send('cd cmake-*')
		shutit.send('./bootstrap --prefix=/usr --system-libs') # not bothering with docs
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
	return cmake(
		'shutit.tk.sd.cmake.cmake', 158844782.014362242,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libarchive.libarchive']
	)

