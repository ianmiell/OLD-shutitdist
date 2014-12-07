"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class nss(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/nss')
		shutit.send('cd /tmp/build/nss')
		shutit.send('curl -L http://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/NSS_3_17_RTM/src/nss-3.17.tar.gz | tar -zxf -')
		shutit.send('cd nss*')
		shutit.send('curl -L http://www.linuxfromscratch.org/patches/blfs/7.6/nss-3.17-standalone-1.patch | patch -Np1 -i -')
		shutit.send('cd nss')
		shutit.send('make BUILD_OPT=1 NSPR_INCLUDE_DIR=/usr/include/nspr USE_SYSTEM_ZLIB=1 ZLIB_LIBS=-lz $([ $(uname -m) = x86_64 ] && echo USE_64=1) $([ -f /usr/include/sqlite3.h ] && echo NSS_USE_SYSTEM_SQLITE=1) -j1')
		shutit.send('cd ../dist')
		shutit.send('install -v -m755 Linux*/lib/*.so /usr/lib')
		shutit.send('install -v -m644 Linux*/lib/{*.chk,libcrmf.a} /usr/lib')
		shutit.send('install -v -m755 -d /usr/include/nss')
		shutit.send('cp -v -RL {public,private}/nss/* /usr/include/nss')
		shutit.send('chmod -v 644 /usr/include/nss/*')
		shutit.send('install -v -m755 Linux*/bin/{certutil,nss-config,pk12util} /usr/bin')
		shutit.send('install -v -m644 Linux*/lib/pkgconfig/nss.pc /usr/lib/pkgconfig')
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
	return nss(
		'shutit.tk.sd.nss.nss', 158844782.0130,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.sqlite.sqlite','shutit.tk.sd.nspr.nspr']
	)

