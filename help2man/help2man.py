"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class help2man(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/help2man')
		shutit.send('cd /tmp/build/help2man')
		shutit.send('mkdir -p /opt/help2man')
		shutit.send('pushd /opt/help2man')
		shutit.send('curl -L http://ftp.gnu.org/gnu/help2man/help2man-' + shutit.cfg[self.module_id]['version'] + '.tar.xz | xz -d | tar -xf -')
		shutit.send('cd help2man-' + shutit.cfg[self.module_id]['version'] + '')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','1.46.4')
		return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/help2man')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return help2man(
		'shutit.tk.sd.help2man.help2man', 158844782.01324135,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.texinfo.texinfo']
	)

