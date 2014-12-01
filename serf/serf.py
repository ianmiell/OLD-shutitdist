"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class serf(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/serf')
		shutit.send('cd /tmp/serf')
		shutit.send('curl http://serf.googlecode.com/svn/src_releases/serf-1.3.8.tar.bz2 | bunzip2 - | tar -xf -')
		shutit.send('pushd serf-*')
		shutit.send('sed -i "/Append/s:RPATH=libdir,::"   SConstruct')
		shutit.send('sed -i "/Default/s:lib_static,::"    SConstruct && sed -i "/Alias/s:install_static,::"  SConstruct && scons PREFIX=/usr')
		shutit.send('scons PREFIX=/usr install')
		shutit.send('cd')
		shutit.send('rm -rf /tmp/serf')
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
	return serf(
		'shutit.tk.sd.serf.serf', 158844782.0151352461436,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.apache_portable_runtime.apache_portable_runtime','shutit.tk.sd.scons.scons']
	)
