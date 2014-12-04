"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class libssl(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		#https://www.openssl.org/source/
		shutit.send('mkdir -p /tmp/build/libssl')
		shutit.send('cd /tmp/build/libssl')
		shutit.send('curl -L https://www.openssl.org/source/openssl-' + shutit.cfg[self.module_id]['version'] + '.tar.gz | tar -zxf -')
		shutit.send('curl -L http://www.linuxfromscratch.org/patches/blfs/svn/openssl-1.0.1j-fix_parallel_build-1.patch > openssl-1.0.1j-fix_parallel_build-1.patch')
		shutit.send('cd openssl-' + shutit.cfg[self.module_id]['version'])
		shutit.send('curl http://www.linuxfromscratch.org/patches/blfs/svn/openssl-1.0.1j-fix_parallel_build-1.patch | patch -Np1 -i -')
		shutit.send('./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib shared zlib-dynamic')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('cd')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','1.0.1j')
		return True

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
	return libssl(
		'shutit.tk.sd.libssl.libssl', 158844782.010125136,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.zlib.zlib']
	)

