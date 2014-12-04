"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class docbookxsl(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/docbookxsl')
		shutit.send('cd /tmp/build/docbookxsl')
		shutit.send('curl -L http://downloads.sourceforge.net/docbook/docbook-xsl-1.78.1.tar.bz2 | bunzip2 -c | tar -xf - --strip-components=1')
		shutit.send('install -v -m755 -d /usr/share/xml/docbook/xsl-stylesheets-1.78.1')
		shutit.send('cp -v -R VERSION common eclipse epub extensions fo highlighting html htmlhelp images javahelp lib manpages params profiling roundtrip slides template tests tools webhelp website xhtml xhtml-1_1 /usr/share/xml/docbook/xsl-stylesheets-1.78.1')
		shutit.send('ln -s VERSION /usr/share/xml/docbook/xsl-stylesheets-1.78.1/VERSION.xsl')
		shutit.send('install -v -m644 -D README /usr/share/doc/docbook-xsl-1.78.1/README.txt')
		shutit.send('install -v -m644    RELEASE-NOTES* NEWS* /usr/share/doc/docbook-xsl-1.78.1')
		shutit.send('if [ ! -d /etc/xml ]; then install -v -m755 -d /etc/xml; fi')
		shutit.send('if [ ! -f /etc/xml/catalog ]; then xmlcatalog --noout --create /etc/xml/catalog; fi')
		shutit.send('xmlcatalog --noout --add "rewriteSystem" "http://docbook.sourceforge.net/release/xsl/1.78.1" "/usr/share/xml/docbook/xsl-stylesheets-1.78.1" /etc/xml/catalog')
		shutit.send('xmlcatalog --noout --add "rewriteURI" "http://docbook.sourceforge.net/release/xsl/1.78.1" "/usr/share/xml/docbook/xsl-stylesheets-1.78.1" /etc/xml/catalog')
		shutit.send('xmlcatalog --noout --add "rewriteSystem" "http://docbook.sourceforge.net/release/xsl/current" "/usr/share/xml/docbook/xsl-stylesheets-1.78.1" /etc/xml/catalog')
		shutit.send('xmlcatalog --noout --add "rewriteURI" "http://docbook.sourceforge.net/release/xsl/current" "/usr/share/xml/docbook/xsl-stylesheets-1.78.1" /etc/xml/catalog')
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
		#shutit.send('rm -rf
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return docbookxsl(
		'shutit.tk.sd.docbookxsl.docbookxsl', 158844782.01112751235,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libxml2.libxml2']
	)

