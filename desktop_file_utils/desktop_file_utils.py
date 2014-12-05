"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class desktop_file_utils(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/desktop_file_utils')
		shutit.send('cd /tmp/build/desktop_file_utils')
		shutit.send('curl -L http://freedesktop.org/software/desktop-file-utils/releases/desktop-file-utils-0.22.tar.xz | xz -d | tar -xf -')
		shutit.send('cd desktop-file-utils*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
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
	return desktop_file_utils(
		'shutit.tk.sd.desktop_file_utils.desktop_file_utils', 158844782.0099,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.glib.glib']
	)

