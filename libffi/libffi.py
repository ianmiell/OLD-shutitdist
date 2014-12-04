"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libffi(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libffi')
		shutit.send('cd /tmp/build/libffi')
		shutit.send('curl -L ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz | tar -zxf -')
		shutit.send('cd libffi-*')
		shutit.send("sed -e '/^includesdir/ s/$(libdir).*$/$(includedir)/' -i include/Makefile.in")
		shutit.send("sed -e '/^includedir/ s/=.*$/=@includedir@/' -e 's/^Cflags: -I${includedir}/Cflags:/' -i libffi.pc.in")
		shutit.send('./configure --prefix=/usr --disable-static')
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

	def finalize(self, shutit):
		#shutit.send('rm -rf
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libffi(
		'shutit.tk.sd.libffi.libffi', 158844782.00121135,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.setup.setup']
	)

