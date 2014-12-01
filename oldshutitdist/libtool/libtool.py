"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class libtool(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.install('git')
		shutit.install('gcc')
		shutit.install('wget')
		shutit.install('m4') # required
		shutit.send('pushd /opt')
		shutit.send('git clone git://git.savannah.gnu.org/libtool.git')
		shutit.send('pushd libtool')
		shutit.send('./bootstrap')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('popd')
		shutit.send('popd')
		shutit.send('rm -rf /opt/libtool')
		shutit.remove('m4') # required
		shutit.remove('git')
		return True

	#def get_config(self, shutit):
	#	return True

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
	return libtool(
		'shutit.tk.sd.libtool.libtool', 0.0225135124,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.help2man.help2man','shutit.tk.sd.texinfo.texinfo','shutit.tk.sd.automake.automake','shutit.tk.sd.git.git','shutit.tk.sd.libxslt.libxslt','shutit.tk.sd.patch.patch']
	)

