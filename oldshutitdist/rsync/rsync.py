"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class rsync(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.install('wget')
		shutit.send('mkdir -p /opt/rsync')
		shutit.send('pushd /opt/rsync')
		shutit.send('wget http://rsync.samba.org/ftp/rsync/src/rsync-' + shutit.cfg[self.module_id]['version'] + '.tar.gz')
		shutit.send('tar -zxf rsync-' + shutit.cfg[self.module_id]['version'] + '.tar.gz')
		shutit.send('pushd rsync-' + shutit.cfg[self.module_id]['version'])
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('popd')
		shutit.send('popd')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','3.1.1')
		return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /opt/rsync')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return rsync(
		'shutit.tk.sd.rsync.rsync', 0.010125,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.make.make']
	)

