"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class sudo(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/sudo')
		shutit.send('cd /tmp/build/sudo')
		shutit.send('curl -L http://www.sudo.ws/sudo/dist/sudo-1.8.10p3.tar.gz | tar -zxf -')
		shutit.send('cd sudo*')
		shutit.send('export EDITOR=vim') # TODO configurable
		shutit.send('./configure --prefix=/usr --libexecdir=/usr/lib --with-all-insults --with-env-editor --docdir=/usr/share/doc/sudo-1.8.10p3 --with-passprompt="[sudo] password for %p"')
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
	return sudo(
		'shutit.tk.sd.sudo.sudo', 158844782.0061,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.vim.vim']
	)

