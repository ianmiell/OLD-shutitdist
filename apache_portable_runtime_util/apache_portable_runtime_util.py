"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class apache_portable_runtime_util(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('mkdir /tmp/build/apr-util')
		shutit.send('cd /tmp/build/apr-util')
		shutit.send('curl http://apache.mirrors.timporter.net/apr/apr-util-' + shutit.cfg[self.module_id]['version'] + '.tar.gz | tar -zxf -')
		shutit.send('cd apr-util*')
		shutit.send('./configure --prefix=/usr --with-apr=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','1.5.4')
		return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/apr-*')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return apache_portable_runtime_util(
		'shutit.tk.sd.apache_portable_runtime_util.apache_portable_runtime_util', 158844782.0121546246,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.apache_portable_runtime.apache_portable_runtime']
	)

