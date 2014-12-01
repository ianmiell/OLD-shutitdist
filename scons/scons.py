"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class scons(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/scons')
		shutit.send('cd /tmp/scons')
		shutit.send('curl https://bitbucket.org/scons/scons/get/45aab7f663f7.zip > scons.zip')
		shutit.send('unzip scons.zip')
		shutit.send('cd scons-*')
		shutit.send('python bootstrap.py')
		shutit.send('python setup.py install --prefix=/usr --standard-lib --optimize=1 --install-data=/usr/share')
		shutit.send('cd')
		#shutit.send('rm -rf /tmp/scons')
		return True

	#def get_config(self, shutit):
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
	return scons(
		'shutit.tk.sd.scons.scons', 158844782.0126264346,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.python2.python2','shutit.tk.sd.zip.zip','shutit.tk.sd.libxml2.libxml2']
	)

