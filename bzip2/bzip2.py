"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class bzip2(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/bzip2/')
		shutit.send('cd /tmp/build/bzip2/')
		shutit.send('curl -L http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz | tar -zxf -')
		shutit.send('cd bzip*')
		shutit.send('curl -L http://www.linuxfromscratch.org/patches/lfs/7.6/bzip2-1.0.6-install_docs-1.patch | patch -Np1 -i -')
		shutit.send(r'''sed -i 's@\(ln -s -f \)$(PREFIX)/bin/@\1@' Makefile''')
		shutit.send('sed -i "s@(PREFIX)/man@(PREFIX)/share/man@g" Makefile')
		shutit.send('make -f Makefile-libbz2_so')
		shutit.send('make clean')
		shutit.send('make')
		shutit.send('make PREFIX=/usr install')
		shutit.send('cp -v bzip2-shared /bin/bzip2')
		shutit.send('cp -av libbz2.so* /lib')
		shutit.send('ln -sv ../../lib/libbz2.so.1.0 /usr/lib/libbz2.so')
		shutit.send('rm -v /usr/bin/{bunzip2,bzcat,bzip2}')
		shutit.send('ln -svf bzip2 /bin/bunzip2')
		shutit.send('ln -svf bzip2 /bin/bzcat')
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
	return bzip2(
		'shutit.tk.sd.bzip2.bzip2', 158844782.0004,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.setup.setup']
	)

