"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class jq(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.install('libonig-dev')
		shutit.send('pushd /opt')
		shutit.send('git clone https://github.com/stedolan/jq.git')
		shutit.send('pushd jq')
# NEEDS install-info - coreutils?
		shutit.send('autoreconf -i')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make -j8')
		shutit.send('make check')
		shutit.send('make install')
		shutit.send('popd')
		shutit.send('popd')
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
		shutit.send('rm -rf /opt/jq')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return jq(
		'shutit.tk.sd.jq.jq', 0.11258107521,
		description='JQ - sed for JSON',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.git.git','shutit.tk.sd.libtool.libtool','shutit.tk.sd.coreutils.coreutils','shutit.tk.sd.flex.flex','shutit.tk.sd.onigurama.onigurama']
	)

