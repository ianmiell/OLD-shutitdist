"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class tls(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/tls')
		shutit.send('cd /tmp/build/tls')
		shutit.send('curl -L ftp://ftp.gnutls.org/gcrypt/gnutls/v3.3/gnutls-3.3.7.tar.xz | xz -d | tar -xf -')
		shutit.send('cd gnutls-*')
		shutit.send(r"sed -i -e '201 i#ifdef ENABLE_PKCS11' -e '213 i#endif' lib/gnutls_privkey.c")
		shutit.send('./configure --prefix=/usr --with-default-trust-store-file=/etc/ssl/ca-bundle.crt')
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
	return tls(
		'shutit.tk.sd.tls.tls', 158844782.01135236,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.nettle.nettle','shutit.tk.sd.pkg_config.pkg_config']
	)

