"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class onigurama(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):

		shutit.run_script('''
			mkdir -p /opt/onigurama
			pushd /opt/onigurama
			wget http://www.geocities.jp/kosako3/oniguruma/archive/onig-5.9.5.tar.gz
			tar -zxf onig-5.9.5.tar.gz
			pushd onig-5.9.5
			./configure --prefix=/usr
			make
			make install
			make install
			popd
			popd
		''')

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

	def finalize(self, shutit):
		shutit.send('rm -rf /opt/onigurama')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return onigurama(
		'shutit.tk.sd.onigurama.onigurama', 0.0101251353136,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.make.make']
	)

