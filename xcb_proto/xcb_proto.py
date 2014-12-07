"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule

class xcb_proto(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/xcb_proto')
		shutit.send('cd /tmp/build/xcb_proto')
		shutit.send('curl -L http://xcb.freedesktop.org/dist/xcb-proto-1.11.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd xcb-proto*')
		shutit.send('./configure $XORG_CONFIG')
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
	return xcb_proto(
		'shutit.tk.sd.xcb_proto.xcb_proto', 158844782.008123,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.python2.python2','shutit.tk.sd.libxml2.libxml2']
	)

