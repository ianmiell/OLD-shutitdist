"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class xmlto(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('mkdir -p /opt/xmlto')
		shutit.send('pushd /opt/xmlto')
		shutit.send('wget https://fedorahosted.org/releases/x/m/xmlto/xmlto-' + shutit.cfg[self.module_id]['version'] + '.tar.bz2')
		shutit.send('bunzip2 xmlto-' + shutit.cfg[self.module_id]['version'] + '.tar.bz2')
		shutit.send('tar -xf xmlto-' + shutit.cfg[self.module_id]['version'] + '.tar')
		shutit.send('pushd xmlto-' + shutit.cfg[self.module_id]['version'])
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('popd')
		shutit.send('popd')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','0.0.26')
		return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /opt/xmlto')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return xmlto(
		'shutit.tk.sd.xmlto.xmlto', 0.01135135,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.make.make']
	)

