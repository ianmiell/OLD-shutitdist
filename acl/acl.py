"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class acl(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/acl')
		shutit.send('cd /tmp/build/acl')
		shutit.send('curl -L http://download.savannah.gnu.org/releases/acl/acl-2.2.52.src.tar.gz | tar -zxf -')
		shutit.send('cd acl*')
		shutit.send('''sed -i -e "/TABS-1;/a if (x > (TABS-1)) x = (TABS-1);" libacl/__acl_to_any_text.c''')
		shutit.send('./configure --prefix=/usr --bindir=/bin')
		shutit.send('make')
		shutit.send('make install install-dev install-lib')
		shutit.send('chmod -v 755 /usr/lib/libacl.so')
		shutit.send('mv -v /usr/lib/libacl.so.* /lib')
		shutit.send('ln -sfv ../../lib/$(readlink /usr/lib/libacl.so) /usr/lib/libacl.so')
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
	return acl(
		'shutit.tk.sd.acl.acl', 158844782.0227,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.attr.attr']
	)

