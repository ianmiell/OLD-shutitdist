"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class readline(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/readline')
		shutit.send('cd /tmp/build/readline')
		shutit.send('curl -L http://ftp.gnu.org/gnu/readline/readline-6.3.tar.gz | tar -zxf -')
		shutit.send('cd readline*')
		shutit.send('curl -L http://www.linuxfromscratch.org/patches/lfs/7.6/readline-6.3-upstream_fixes-2.patch | patch -Np1 -i -')
		shutit.send('''sed -i '/MV.*old/d' Makefile.in''')
		shutit.send('''sed -i '/{OLDSUFF}/c:' support/shlib-install''')
		shutit.send('./configure --prefix=/usr --docdir=/usr/share/doc/readline-6.3')
		shutit.send('make SHLIB_LIBS=-lncurses')
		shutit.send('make SHLIB_LIBS=-lncurses install')
		shutit.send('mv -v /usr/lib/lib{readline,history}.so.* /lib')
		shutit.send('ln -sfv ../../lib/$(readlink /usr/lib/libreadline.so) /usr/lib/libreadline.so')
		shutit.send('ln -sfv ../../lib/$(readlink /usr/lib/libhistory.so ) /usr/lib/libhistory.so')
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
	return readline(
		'shutit.tk.sd.readline.readline', 158844782.00141253,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.ncurses.ncurses']
	)

