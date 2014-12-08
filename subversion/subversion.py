"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class subversion(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/subversion')
		shutit.send('cd /tmp/build/subversion')
		shutit.send('curl -L http://mirror.gopotato.co.uk/apache/subversion/subversion-' + shutit.cfg[self.module_id]['version'] + '.tar.gz | tar -zxf -')
		shutit.send('cd subversion-' + shutit.cfg[self.module_id]['version'])
		shutit.send('./configure --with-serf=/usr --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','1.8.10')
		return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		return True

	#def remove(self, shutit):
	#	return True

	def test(self, shutit):
		shutit.send('mkdir -p /tmp/shutit')
		shutit.send('cd /tmp/shutit')
		shutit.send('svn co https://github.com/ianmiell/shutit')
		return True

def module():
	return subversion(
		'shutit.tk.sd.subversion.subversion', 158844782.0078,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.apache_portable_runtime_util.apache_portable_runtime_util','shutit.tk.sd.sqlite.sqlite','shutit.tk.sd.serf.serf','shutit.tk.sd.autoconf.autoconf']
	)

