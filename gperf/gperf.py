"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class gperf(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/gperf')
		shutit.send('cd /tmp/build/gperf')
		shutit.send('curl -L http://ftp.gnu.org/pub/gnu/gperf/gperf-' + shutit.cfg[self.module_id]['version'] + '.tar.gz | tar -zxf -')
		shutit.send('cd gperf-' + shutit.cfg[self.module_id]['version'])
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','3.0.4')
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
	return gperf(
		'shutit.tk.sd.gperf.gperf', 158844782.004,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.setup.setup']
	)

