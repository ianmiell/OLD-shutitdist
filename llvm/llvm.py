"""ShutIt module. See http://shutit.tk
In source, line 16 should be blank, within the build def. This doesn't matter except for test builds, so can be removed once in use.
"""

from shutit_module import ShutItModule


class llvm(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/llvm')
		shutit.send('cd /tmp/build/llvm')
		shutit.send('tar -xvf http://llvm.org/releases/3.5.0/llvm-3.5.0.src.tar.xz | xz -d | tar -xf -')
		shutit.send('cd llvm-3.5.0')
		shutit.send('sed -e "s:/docs/llvm:/share/doc/llvm-3.5.0:" -i Makefile.config.in')
		shutit.send('CC=gcc CXX=g++ ./configure --prefix=/usr --sysconfdir=/etc --enable-libffi --enable-optimized --enable-shared --disable-assertions')
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
	return llvm(
		'shutit.tk.sd.llvm.llvm', 158844782.00,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.python2.python2']
	)

