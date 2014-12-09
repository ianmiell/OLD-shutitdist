"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class jq(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('cd /tmp/build')
		shutit.send('git clone https://github.com/stedolan/jq.git')
		shutit.send('cd jq')
		shutit.send('autoreconf -i')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make check')
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
		#shutit.send('rm -rf
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return jq(
		'shutit.tk.sd.jq.jq', 158844782.00807,
		description='JQ - sed for JSON',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.git.git','shutit.tk.sd.libtool.libtool','shutit.tk.sd.onigurama.onigurama','shutit.tk.sd.flex.flex']
	)

