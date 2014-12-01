"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libxslt(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/libxslt')
		shutit.send('cd /tmp/libxslt')
		shutit.send('curl -L http://xmlsoft.org/sources/libxslt-' + shutit.cfg[self.module_id]['version'] + '.tar.gz | tar -zxf -')
		shutit.send('cd libxslt-*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('cd')
		#shutit.send('rm -rf /tmp/libxslt')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','1.1.28')
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
	return libxslt(
		'shutit.tk.sd.libxslt.libxslt', 158844782.01231251324,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libxml2.libxml2']
	)
