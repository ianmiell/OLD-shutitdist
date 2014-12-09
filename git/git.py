"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class git(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/git')
		shutit.send('cd /tmp/build/git')
		shutit.send('curl -L https://www.kernel.org/pub/software/scm/git/git-2.1.0.tar.xz | xz -d | tar -xf -')
		shutit.send('cd git-*')
		#shutit.send('make prefix=/usr all doc info') # trouble with docs/docbook etc - to resolve
		shutit.send('./configure --prefix=/usr --with-gitconfig=/etc/gitconfig')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	return True

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
	return git(
		'shutit.tk.sd.git.git', 158844782.00806,
		description='Git built from source',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.python2.python2']
	)

