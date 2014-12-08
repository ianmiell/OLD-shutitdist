"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class glib_config(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/glib1')
		shutit.send('cd /tmp/build/glib1')
		shutit.send('curl -L http://gd.tuwien.ac.at/graphics/gimp/gtk/v1.2/glib-1.2.10.tar.gz | tar -zxf -')
		shutit.send('curl -L http://www.linuxfromscratch.org/blfs/downloads/6.1/glib-1.2.10-gcc34-1.patch | patch -Np1 -i -')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('chmod -v 755 /usr/lib/libgmodule-1.2.so.0.0.10')
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
	return glib_config(
		'shutit.tk.sd.glib_config.glib_config', 158844782.00115,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.setup.setup']
	)

