"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class yacc(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/byacc')
		shutit.send('cd /tmp/build/byacc')
		shutit.send('mkdir -p byacc')
		shutit.send('cd /tmp/build/byacc')
		shutit.send('curl -L http://invisible-island.net/datafiles/release/byacc.tar.gz | tar -zxf -')
		shutit.send('cd byacc*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/byacc')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return yacc(
		'shutit.tk.sd.yacc.yacc', 158844782.0121325,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.setup.setup']
	)

