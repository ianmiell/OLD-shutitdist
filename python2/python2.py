"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class python2(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir /tmp/python')
		shutit.send('cd /tmp/python')
		shutit.send('curl https://www.python.org/ftp/python/2.7.9/Python-2.7.9rc1.tar.xz | xz -d | tar -xf -')
		shutit.send('cd Python-*')
		shutit.send('./configure --prefix=/usr --enable-shared')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('mkdir -p /usr/include/python2.7/')
		shutit.send('cp Include/* /usr/include/python2.7/')
		shutit.send('cd')
		#shutit.send('rm -rf /tmp/python')
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
	return python2(
		'shutit.tk.sd.python2.python2', 158844782.0012516436,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.setup.setup']
	)

