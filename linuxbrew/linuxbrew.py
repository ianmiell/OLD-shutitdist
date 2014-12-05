"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class linuxbrew(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('pushd /opt')
		shutit.send('git clone https://github.com/Homebrew/linuxbrew.git ~/.linuxbrew')
		shutit.send('''echo 'export PATH="$HOME/.linuxbrew/bin:$PATH"' >> ~/.bashrc''')
		shutit.send('''echo 'export LD_LIBRARY_PATH="$HOME/.linuxbrew/lib:$LD_LIBRARY_PATH"' >> ~/.bashrc''')
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
	return linuxbrew(
		'shutit.tk.sd.linuxbrew.linuxbrew', 158844782.0083,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.texinfo.texinfo','shutit.tk.sd.expat.expat','shutit.tk.sd.ncurses.ncurses','shutit.tk.sd.git.git']
	)

