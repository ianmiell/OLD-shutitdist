"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class docbook(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('mkdir -p /opt/docbook')
		shutit.send('pushd /opt/docbook')
		version = shutit.cfg[self.module_id]['version']
		shutit.send('wget http://www.docbook.org/xml/' + version + '/docbook-xml-' + version + '.zip')
		shutit.send('unzip docbook-xml-' + version + '.zip')
		shutit.send('install -v -m755 -d /usr/share/xml/docbook/xsl-stylesheets-1.78.1')
		shutit.run_script('''
			install -v -d -m755 /usr/share/xml/docbook/xml-dtd-4.5 &&
			install -v -d -m755 /etc/xml &&
			chown -R root:root . &&
			cp -v -af docbook.cat *.dtd ent/ *.mod \
			    /usr/share/xml/docbook/xml-dtd-4.5
		''')
		shutit.run_script('''
			if [ ! -e /etc/xml/docbook ]; then
			    xmlcatalog --noout --create /etc/xml/docbook
			fi &&
			xmlcatalog --noout --add "public" \
			    "-//OASIS//DTD DocBook XML V4.5//EN" \
			    "http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd" \
			    /etc/xml/docbook &&
			xmlcatalog --noout --add "public" \
			    "-//OASIS//DTD DocBook XML CALS Table Model V4.5//EN" \
			    "file:///usr/share/xml/docbook/xml-dtd-4.5/calstblx.dtd" \
			    /etc/xml/docbook &&
			xmlcatalog --noout --add "public" \
			    "-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
			    "file:///usr/share/xml/docbook/xml-dtd-4.5/soextblx.dtd" \
			    /etc/xml/docbook &&
			xmlcatalog --noout --add "public" \
			    "-//OASIS//ELEMENTS DocBook XML Information Pool V4.5//EN" \
			    "file:///usr/share/xml/docbook/xml-dtd-4.5/dbpoolx.mod" \
			    /etc/xml/docbook &&
			xmlcatalog --noout --add "public" \
			    "-//OASIS//ELEMENTS DocBook XML Document Hierarchy V4.5//EN" \
			    "file:///usr/share/xml/docbook/xml-dtd-4.5/dbhierx.mod" \
			    /etc/xml/docbook &&
			xmlcatalog --noout --add "public" \
			    "-//OASIS//ELEMENTS DocBook XML HTML Tables V4.5//EN" \
			    "file:///usr/share/xml/docbook/xml-dtd-4.5/htmltblx.mod" \
			    /etc/xml/docbook &&
			xmlcatalog --noout --add "public" \
			    "-//OASIS//ENTITIES DocBook XML Notations V4.5//EN" \
			    "file:///usr/share/xml/docbook/xml-dtd-4.5/dbnotnx.mod" \
			    /etc/xml/docbook &&
			xmlcatalog --noout --add "public" \
			    "-//OASIS//ENTITIES DocBook XML Character Entities V4.5//EN" \
			    "file:///usr/share/xml/docbook/xml-dtd-4.5/dbcentx.mod" \
			    /etc/xml/docbook &&
			xmlcatalog --noout --add "public" \
			    "-//OASIS//ENTITIES DocBook XML Additional General Entities V4.5//EN" \
			    "file:///usr/share/xml/docbook/xml-dtd-4.5/dbgenent.mod" \
			    /etc/xml/docbook &&
			xmlcatalog --noout --add "rewriteSystem" \
			    "http://www.oasis-open.org/docbook/xml/4.5" \
			    "file:///usr/share/xml/docbook/xml-dtd-4.5" \
			    /etc/xml/docbook &&
			xmlcatalog --noout --add "rewriteURI" \
			    "http://www.oasis-open.org/docbook/xml/4.5" \
			    "file:///usr/share/xml/docbook/xml-dtd-4.5" \
			    /etc/xml/docbook
		''')
		shutit.run_script('''
			if [ ! -e /etc/xml/catalog ]; then
			    xmlcatalog --noout --create /etc/xml/catalog
			fi &&
			xmlcatalog --noout --add "delegatePublic" \
			    "-//OASIS//ENTITIES DocBook XML" \
			    "file:///etc/xml/docbook" \
			    /etc/xml/catalog &&
			xmlcatalog --noout --add "delegatePublic" \
			    "-//OASIS//DTD DocBook XML" \
			    "file:///etc/xml/docbook" \
			    /etc/xml/catalog &&
			xmlcatalog --noout --add "delegateSystem" \
			    "http://www.oasis-open.org/docbook/" \
			    "file:///etc/xml/docbook" \
			    /etc/xml/catalog &&
			xmlcatalog --noout --add "delegateURI" \
			    "http://www.oasis-open.org/docbook/" \
			    "file:///etc/xml/docbook" \
			    /etc/xml/catalog
		''')
		shutit.send('popd')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','4.5')
		return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /opt/docbook')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return docbook(
		'shutit.tk.sd.docbook.docbook', 0.01124918274,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.zip.zip']
	)

