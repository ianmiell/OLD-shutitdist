"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class subversion(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('mkdir -p /opt/subversion')
		shutit.send('pushd /opt/subversion')
		shutit.send('wget http://mirror.gopotato.co.uk/apache/subversion/subversion-' + shutit.cfg[self.module_id]['version'] + '.tar.gz')
		shutit.send('tar -zxf subversion-' + shutit.cfg[self.module_id]['version'] + '.tar.gz')
		shutit.send('pushd subversion-' + shutit.cfg[self.module_id]['version'])
		shutit.send('./configure --with-serf=/usr --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('popd')
		shutit.send('popd')
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
		shutit.send('rm -rf /opt/subversion')
		return True

	#def remove(self, shutit):
	#	return True

	def test(self, shutit):
		shutit.send('mkdir -p /tmp/shutit')
		shutit.send('pushd /tmp/shutit')
		shutit.send('svn co https://github.com/ianmiell/shutit')
		shutit.send('popd /tmp/shutit')
		shutit.send('rm -rf /tmp/shutit')
		return True

def module():
	return subversion(
		'shutit.tk.sd.subversion.subversion', 0.205532473,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.apache_portable_runtime_util.apache_portable_runtime_util','shutit.tk.sd.sqlite.sqlite','shutit.tk.sd.serf.serf','shutit.tk.sd.autoconf.autoconf','shutit.tk.sd.libtool.libtool']
	)

