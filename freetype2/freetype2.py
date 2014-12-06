"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class freetype2(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
        shutit.send('mkdir -p /tmp/build/harfbuzz')
        shutit.send('cd /tmp/build/harfbuzz')
        shutit.send('curl -L http://www.freedesktop.org/software/harfbuzz/release/harfbuzz-0.9.35.tar.bz2 | bunzip2 -c | tar -xf -')
        shutit.send('cd harfbuzz*')
        shutit.send('./configure --prefix=/usr --with-gobject')
        shutit.send('make')
        shutit.send('make install')
		shutit.send('mkdir -p /tmp/build/freetype2')
		shutit.send('cd /tmp/build/freetype2')
		shutit.send('curl -L http://downloads.sourceforge.net/freetype/freetype-2.5.3.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd freetype*')
		shutit.send('sed -i  -e "/AUX.*.gxvalid/s@^# @@" -e "/AUX.*.otvalid/s@^# @@" modules.cfg')
		shutit.send(r'''sed -ri -e 's:.*(#.*SUBPIXEL.*) .*:\1:' include/config/ftoption.h''')
		shutit.send('./configure --prefix=/usr --disable-static')
		shutit.send('make')
		shutit.send('make install')
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
	return freetype2(
		'shutit.tk.sd.freetype2.freetype2', 158844782.0098,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.which.which','shutit.tk.sd.harfbuzz.harfbuzz','shutit.tk.sd.libpng.libpng','shutit.tk.sd.glib.glib','shutit.tk.sd.freetype.freetype']
	)

