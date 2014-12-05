"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class wget(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/wget')
		shutit.send('cd /tmp/build/wget')
		shutit.send('curl -L http://ftp.gnu.org/gnu/wget/wget-1.15.tar.xz | xz -d | tar -xf -')
		shutit.send('cd wget*')
		shutit.send('./configure --prefix=/usr --sysconfdir=/etc --with-ssl=openssl')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('echo ca-directory=/etc/ssl/certs >> /etc/wgetrc')
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
	return wget(
		'shutit.tk.sd.wget.wget', 158844782.0022,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.openssl.openssl']
	)

