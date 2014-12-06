"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class berkeleydb(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
#http://download.oracle.com/berkeley-db/db-6.1.19.tar.gz
#cd build_unix                        &&
#../dist/configure --prefix=/usr      \
#                  --enable-compat185 \
#                  --enable-dbm       \
#                  --disable-static   \
#                  --enable-cxx       &&
#make
#make docdir=/usr/share/doc/db-6.1.19 install &&
#chown -v -R root:root                        \
#      /usr/bin/db_*                          \
#      /usr/include/db{,_185,_cxx}.h          \
#      /usr/lib/libdb*.{so,la}                \
#      /usr/share/doc/db-6.1.19


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
	return berkeleydb(
		'shutit.tk.sd.berkeleydb.berkeleydb', 158844782.0011,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.tcl.tcl','shutit.tk.sd.openjdk.openjdk','shutit.tk.sd.sharutils.sharutils']
	)

