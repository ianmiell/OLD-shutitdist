"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class git(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/git')
		shutit.send('cd /tmp/build/git')
		shutit.send('curl -L https://github.com/git/git/archive/master.zip > master.zip')
		shutit.send('unzip master.zip')
		shutit.send('cd git-master')
		#shutit.send('make prefix=/usr all doc info') # trouble with docs/docbook etc - to resolve
		shutit.send('make prefix=/usr all')
		shutit.send('make install prefix=/usr')
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
		'shutit.tk.sd.git.git', 158844782.0071,
		description='Git built from source',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.zip.zip','shutit.tk.sd.tcl.tcl','shutit.tk.sd.expat.expat','shutit.tk.sd.asciidoc.asciidoc','shutit.tk.sd.xmlto.xmlto','shutit.tk.sd.libxslt.libxslt','shutit.tk.sd.openssl.openssl','shutit.tk.sd.gettext.gettext']
	)

