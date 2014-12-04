"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class flex(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/flex')
		shutit.send('cd /tmp/build/flex')
		shutit.send('curl -L http://prdownloads.sourceforge.net/flex/flex-' + shutit.cfg[self.module_id]['version'] + '.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd flex-' + shutit.cfg[self.module_id]['version'])
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','2.5.39')
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
	return flex(
		'shutit.tk.sd.flex.flex', 158844782.0122515332,
		description='Flex',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.setup.setup']
	)

