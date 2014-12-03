"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class gettext(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/gettext')
		shutit.send('cd /tmp/build/gettext')
		shutit.send('curl -L http://ftp.gnu.org/pub/gnu/gettext/gettext-0.19.3.tar.xz | xz -d | tar -xf -')
		shutit.send('cd gettext-*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make check')
		shutit.send('make install')
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

	#def finalize(self, shutit):
	#	return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return gettext(
		'shutit.tk.sd.gettext.gettext', 158844782.0124125236240,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.setup.setup']
	)

