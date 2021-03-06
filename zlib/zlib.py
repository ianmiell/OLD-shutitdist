"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class zlib(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		#From http://www.zlib.net/
		shutit.send('mkdir -p /tmp/build/zlib')
		shutit.send('cd /tmp/build/zlib')
		shutit.send('curl http://zlib.net/zlib-' + shutit.cfg[self.module_id]['version'] + '.tar.gz | tar -zxf -')
		shutit.send('cd zlib-' + shutit.cfg[self.module_id]['version'])
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('mkdir -p /tmp/build/zlib_headers')
		shutit.send('cp -r * /tmp/build/zlib_headers')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','1.2.8')
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
	return zlib(
		'shutit.tk.sd.zlib.zlib', 158844782.0009,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.automake.automake']
	)

