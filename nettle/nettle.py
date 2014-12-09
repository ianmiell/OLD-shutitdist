"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class nettle(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/nettle')
		shutit.send('cd /tmp/build/nettle')
		shutit.send('curl -L http://ftp.gnu.org/gnu/nettle/nettle-' + shutit.cfg[self.module_id]['version'] + '.tar.gz | tar -zxf -')
		shutit.send('cd /tmp/build/nettle/nettle-*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		# Using earlier version due to dep issue, so ignoring these linux from scratch lines.
		#shutit.send('chmod -v 755 /usr/lib/libhogweed.so.2.5 /usr/lib/libnettle.so.4.7') # requires gmp
		#shutit.send('install -v -m755 -d /usr/share/doc/nettle-2.7.1')
		#shutit.send('install -v -m644 nettle.html /usr/share/doc/nettle-2.7.1')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','2.6')
		return True

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
	return nettle(
		'shutit.tk.sd.nettle.nettle', 158844782.0079,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.gmp.gmp','shutit.tk.sd.pkg_config.pkg_config','shutit.tk.sd.subversion.subversion','shutit.tk.sd.libxslt.libxslt']
	)

