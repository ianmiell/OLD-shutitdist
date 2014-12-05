"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class vim(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/vim')
		shutit.send('cd /tmp/build/vim')
		shutit.send('curl -L ftp://ftp.vim.org/pub/vim/unix/vim-7.4.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd vim*')
		shutit.send('''echo '#define SYS_VIMRC_FILE "/etc/vimrc"' >> src/feature.h''')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('ln -svf vim /usr/bin/vi')
		shutit.send('for L in  /usr/share/man/{,*/}man1/vim.1; do ln -sv vim.1 $(dirname $L)/vi.1; done')
		shutit.send('ln -sv ../vim/vim74/doc /usr/share/doc/vim-7.4')
		shutit.send('''cat > /etc/vimrc << "EOF"
		" Begin /etc/vimrc
		
		set nocompatible
		set backspace=2
		syntax on
		if (&term == "iterm") || (&term == "putty")
		  set background=dark
		endif
		
		" End /etc/vimrc
		EOF''')
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
	return vim(
		'shutit.tk.sd.vim.vim', 158844782.0045,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.ncurses.ncurses']
	)

