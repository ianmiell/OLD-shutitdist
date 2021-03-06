"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class libtool(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libtool')
		shutit.send('cd /tmp/build/libtool')
		shutit.send('curl -L http://ftp.gnu.org/gnu/libtool/libtool-2.4.2.tar.gz | tar -zxf -')
		shutit.send('cd libtool*')
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

	#def finalize(self, shutit):
	#	#shutit.send('rm -rf
	#	return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libtool(
		'shutit.tk.sd.libtool.libtool', 158844782.0073,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.help2man.help2man','shutit.tk.sd.texinfo.texinfo','shutit.tk.sd.automake.automake','shutit.tk.sd.libxslt.libxslt']
	)

