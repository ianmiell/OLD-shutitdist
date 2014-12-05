"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class java_binary(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
#http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.7.0.65/OpenJDK-1.7.0.65-x86_64-bin.tar.xz

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
	return java_binary(
		'shutit.tk.sd.java_binary.java_binary', 158844782.00117,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.alsa_lib.alsa_lib']
	)

