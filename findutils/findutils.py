"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class findutils(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/findutils')
		shutit.send('cd /tmp/build/findutils')
		shutit.send('curl -L http://ftp.gnu.org/gnu/findutils/findutils-4.4.2.tar.gz | tar -zxf -')
		shutit.send('cd findutils*')
		shutit.send('./configure --prefix=/usr --localstatedir=/var/lib/locate')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('mv -v /usr/bin/find /bin')
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
	return findutils(
		'shutit.tk.sd.findutils.findutils', 158844782.00102,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.setup.setup']
	)

