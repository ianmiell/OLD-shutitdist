"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class iproute2(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/iproute2')
		shutit.send('cd /tmp/build/iproute2')
		shutit.send('curl -L https://www.kernel.org/pub/linux/utils/net/iproute2/iproute2-3.16.0.tar.xz | xz -d | tar -xf -')
		shutit.send('cd iproute*')
		shutit.send("sed -i '/^TARGETS/s@arpd@@g' misc/Makefile")
		shutit.send('sed -i /ARPD/d Makefile')
		shutit.send("sed -i 's/arpd.8//' man/man8/Makefile")
		shutit.send('make')
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
	return iproute2(
		'shutit.tk.sd.iproute2.iproute2', 158844782.01212523465,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.setup.setup','shutit.tk.sd.bison.bison']
	)

