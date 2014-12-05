"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class expat(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/expat')
		shutit.send('cd /tmp/build/expat')
		shutit.send('curl -L expat.tar.gz http://downloads.sourceforge.net/project/expat/expat/' + shutit.cfg[self.module_id]['version'] + '/expat-' + shutit.cfg[self.module_id]['version'] + '.tar.gz | tar -zxf -')
		shutit.send('cd expat-' + shutit.cfg[self.module_id]['version'])
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','2.1.0')
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
	return expat(
		'shutit.tk.sd.expat.expat', 158844782.0059,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.setup.setup']
	)

