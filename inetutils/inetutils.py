"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class inetutils(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/inetutils')
		shutit.send('cd /tmp/build/inetutils')
		shutit.send('curl -L http://ftp.gnu.org/gnu/inetutils/inetutils-1.9.2.tar.gz | tar -zxf -')
		shutit.send('cd inetutils*')
		shutit.send('''echo '#define PATH_PROCNET_DEV "/proc/net/dev"' >> ifconfig/system/linux.h''')
		shutit.send('./configure --prefix=/usr --localstatedir=/var --disable-logger --disable-whois --disable-servers')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('mv -v /usr/bin/{hostname,ping,ping6,traceroute} /bin')
		shutit.send('mv -v /usr/bin/ifconfig /sbin')
		shutit.send('./configure --prefix=/usr')
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
	return inetutils(
		'shutit.tk.sd.inetutils.inetutils', 158844782.0047,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.pkg_config.pkg_config']
	)

