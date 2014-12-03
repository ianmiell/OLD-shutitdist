"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class libxml2(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libxml2')
		shutit.send('cd /tmp/build/libxml2')
		shutit.send('curl http://xmlsoft.org/sources/libxml2-sources-' + shutit.cfg[self.module_id]['version'] + '.tar.gz | tar -zxf -')
		shutit.send('cd libxml2-' + shutit.cfg[self.module_id]['version'])
		shutit.send(r"sed -e /xmlInitializeCatalog/d -e 's/((ent->checked =.*&&/(((ent->checked == 0) || ((ent->children == NULL) \&\& (ctxt->options \& XML_PARSE_NOENT))) \&\&/' -i parser.c")
		shutit.send('./configure --prefix=/usr --disable-static --with-history')
		shutit.send('make')
		shutit.send('make install')
		#shutit.send('rm -rf /tmp/libxml2')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','2.9.2')
		return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libxml2')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libxml2(
		'shutit.tk.sd.libxml2.libxml2', 158844782.011125135,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.python2.python2']
	)

