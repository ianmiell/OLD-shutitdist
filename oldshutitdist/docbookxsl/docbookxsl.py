"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class docbookxsl(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('mkdir -p /opt/docbookxsl')
		shutit.send('pushd /opt/docbookxsl')
		shutit.send('wget http://downloads.sourceforge.net/docbook/docbook-xsl-' + shutit.cfg[self.module_id]['version'] + '.tar.bz2')
		shutit.send('bunzip2 docbook-xsl-' + shutit.cfg[self.module_id]['version'] + '.tar.bz2')
		shutit.send('tar -xf docbook-xsl-' + shutit.cfg[self.module_id]['version'] + '.tar --strip-components=1')
		# www.linuxfromscratch.org/blfs/view/svn/pst/docbook-xsl.html for installation TODO
		shutit.run_script('''
			install -v -m755 -d /usr/share/xml/docbook/xsl-stylesheets-1.78.1 &&
			
			cp -v -R VERSION common eclipse epub extensions fo highlighting html \
			         htmlhelp images javahelp lib manpages params profiling \
			         roundtrip slides template tests tools webhelp website \
			         xhtml xhtml-1_1 \
			    /usr/share/xml/docbook/xsl-stylesheets-1.78.1 &&
			
			ln -s VERSION /usr/share/xml/docbook/xsl-stylesheets-1.78.1/VERSION.xsl &&
			
			install -v -m644 -D README \
			                    /usr/share/doc/docbook-xsl-1.78.1/README.txt &&
			install -v -m644    RELEASE-NOTES* NEWS* \
			                    /usr/share/doc/docbook-xsl-1.78.1

			if [ ! -d /etc/xml ]; then install -v -m755 -d /etc/xml; fi &&
			if [ ! -f /etc/xml/catalog ]; then
			    xmlcatalog --noout --create /etc/xml/catalog
			fi &&
			
			xmlcatalog --noout --add "rewriteSystem" \
			           "http://docbook.sourceforge.net/release/xsl/1.78.1" \
			           "/usr/share/xml/docbook/xsl-stylesheets-1.78.1" \
			    /etc/xml/catalog &&
			
			xmlcatalog --noout --add "rewriteURI" \
			           "http://docbook.sourceforge.net/release/xsl/1.78.1" \
			           "/usr/share/xml/docbook/xsl-stylesheets-1.78.1" \
			    /etc/xml/catalog &&
			
			xmlcatalog --noout --add "rewriteSystem" \
			           "http://docbook.sourceforge.net/release/xsl/current" \
			           "/usr/share/xml/docbook/xsl-stylesheets-1.78.1" \
			    /etc/xml/catalog &&
			
			xmlcatalog --noout --add "rewriteURI" \
			           "http://docbook.sourceforge.net/release/xsl/current" \
			           "/usr/share/xml/docbook/xsl-stylesheets-1.78.1" \
			    /etc/xml/catalog
		''')
		shutit.send('popd')
		# Save space
		shutit.send('strip --strip-debug /tools/lib/*')
		shutit.send('/usr/bin/strip --strip-unneeded /tools/{,s}bin/*')
		shutit.send('rm -rf /tools/{,share}/{info,man,doc}')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','1.78.1')
		return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /opt/docbookxsl')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return docbookxsl(
		'shutit.tk.sd.docbookxsl.docbookxsl', 0.011318728,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.libxslt.libxslt']
	)

