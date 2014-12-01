"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class apache_portable_runtime(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('cd /tmp')
		shutit.send('curl http://apache.mirrors.timporter.net//apr/apr-' + shutit.cfg[self.module_id]['version'] + '.tar.gz | tar -zxf -')
		shutit.send('cd apr-' + shutit.cfg[self.module_id]['version'])
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('cd')
		shutit.send('rm -rf /tmp/apr-*')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','1.5.1')
		return True

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
	return apache_portable_runtime(
		'shutit.tk.sd.apache_portable_runtime.apache_portable_runtime', 158844782.01213613624,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.setup.setup']
	)

