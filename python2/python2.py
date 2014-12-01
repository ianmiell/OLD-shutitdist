"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class python2(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir /tmp/python')
		shutit.send('cd /tmp/python')
		shutit.send('curl http://www.python.org/ftp/python/2.7.8/Python-2.7.8.tar.xz | xz -d | tar -xf -')
		shutit.send('cd Python-*')
		shutit.send('./configure --prefix=/usr --enable-shared --with-system-expat --with-system-ffi --enable-unicode=ucs4')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('chmod -v 755 /usr/lib/libpython2.7.so.1.0')
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

