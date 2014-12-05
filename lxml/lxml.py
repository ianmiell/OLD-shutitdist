"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class lxml(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/lxml')
		shutit.send('cd /tmp/build/lxml')
		shutit.send('curl -L https://github.com/lxml/lxml/archive/master.zip > master.zip')
		shutit.send('unzip master.zip')
		shutit.send('cd lxml-*')
		shutit.pause_point('')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

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
	return lxml(
		'shutit.tk.sd.lxml.lxml', 158844782.0046,
		description='',
		maintainer='',
		depends=['shutit.tk.libxslt']
	)

