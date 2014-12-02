"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class curl(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/curl')
		shutit.send('cd /tmp/build/curl')
		shutit.send('curl -L http://curl.haxx.se/download/curl-7.37.1.tar.bz2 | bunzip2 - | tar -xf -')
		shutit.send('cd curl-*')
		shutit.send('./configure --prefix=/usr --disable-static --enable-threaded-resolver')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('find docs \( -name "Makefile*" -o -name "*.1" -o -name "*.3" \) -exec rm {} \;')
		shutit.send('install -v -d -m755 /usr/share/doc/curl-7.37.1')
		shutit.send('cp -v -R docs/*     /usr/share/doc/curl-7.37.1')
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
	return curl(
		'shutit.tk.sd.curl.curl', 158844782.01351987515,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.openssl.openssl','shutit.tk.sd.tls.tls']
	)

