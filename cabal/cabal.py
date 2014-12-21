"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class cabal(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('apt-get install -y ghc haddock')
		shutit.send('mkdir -p /tmp/build/cabal')
		shutit.send('cd /tmp/build/cabal')
		#shutit.send('curl -L https://www.haskell.org/cabal/release/cabal-1.20.0.2/Cabal-1.20.0.2.tar.gz | tar -zxf -')
		shutit.send('curl -L https://www.haskell.org/cabal/release/cabal-install-1.20.0.3/cabal-install-1.20.0.3.tar.gz | tar -zxf -')
		shutit.send('cd cabal-*')
		shutit.send('./bootstrap.sh')
  		shutit.send('cp /root/.cabal/bin/cabal /usr/bin/')
  		shutit.send('cabal update')
		shutit.send('cabal install cabal-install')
		shutit.send('cp /root/.cabal/bin/cabal /usr/bin/cabal')
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
	return cabal(
		'shutit.tk.sd.cabal.cabal', 158844782.00151,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.setup.setup']
	)

