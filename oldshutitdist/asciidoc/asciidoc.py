"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class asciidoc(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		#http://www.methods.co.nz/asciidoc/INSTALL.html#X1
		shutit.send('mkdir -p /opt/asciidoc')
		shutit.send('pushd /opt/asciidoc')
		shutit.send('wget http://downloads.sourceforge.net/project/asciidoc/asciidoc/' + shutit.cfg[self.module_id]['version'] + '/asciidoc-' + shutit.cfg[self.module_id]['version'] + '.tar.gz')
		shutit.send('tar -zxf asciidoc-' + shutit.cfg[self.module_id]['version'] + '.tar.gz')
		shutit.send('pushd asciidoc-' + shutit.cfg[self.module_id]['version'])
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('popd')
		shutit.send('popd')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','8.6.9')
		return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /opt/asciidoc')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return asciidoc(
		'shutit.tk.sd.asciidoc.asciidoc', 0.0125243623,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.python.python']
	)

