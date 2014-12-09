"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class ncurses(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/ncurses')
		shutit.send('cd /tmp/build/ncurses')
		shutit.send('curl -L http://ftp.gnu.org/gnu//ncurses/ncurses-5.9.tar.gz | tar -zxf -')
		shutit.send('cd ncurses*')
		shutit.send('./configure --prefix=/usr --mandir=/usr/share/man --with-shared --without-debug --enable-pc-files --enable-widec')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('mv -v /usr/lib/libncursesw.so.5* /lib')
		shutit.send('ln -sfv ../../lib/$(readlink /usr/lib/libncursesw.so) /usr/lib/libncursesw.so')
		shutit.run_script('''for lib in ncurses form panel menu ; do
		    rm -vf                    /usr/lib/lib${lib}.so
		    echo "INPUT(-l${lib}w)" > /usr/lib/lib${lib}.so
		    ln -sfv lib${lib}w.a      /usr/lib/lib${lib}.a
		    ln -sfv ${lib}w.pc        /usr/lib/pkgconfig/${lib}.pc
		done''')
		shutit.send('ln -sfv libncurses++w.a /usr/lib/libncurses++.a')
		shutit.send('rm -vf                     /usr/lib/libcursesw.so')
		shutit.send('echo "INPUT(-lncursesw)" > /usr/lib/libcursesw.so')
		shutit.send('ln -sfv libncurses.so      /usr/lib/libcurses.so')
		shutit.send('ln -sfv libncursesw.a      /usr/lib/libcursesw.a')
		shutit.send('ln -sfv libncurses.a       /usr/lib/libcurses.a')
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
	return ncurses(
		'shutit.tk.sd.ncurses.ncurses', 158844782.0025,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.pkg_config.pkg_config']
	)

