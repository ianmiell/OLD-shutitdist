"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class docbookxml(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/docbookxml')
		shutit.send('cd /tmp/build/docbookxml')
		shutit.send('curl -L http://www.docbook.org/xml/4.5/docbook-xml-4.5.zip > docbook_xml.zip')
		shutit.send('unzip docbook_xml.zip')
		shutit.send('install -v -d -m755 /usr/share/xml/docbook/xml-dtd-4.5')
		shutit.send('install -v -d -m755 /etc/xml')
		shutit.send('chown -R root:root .')
		shutit.send('cp -v -af docbook.cat *.dtd ent/ *.mod /usr/share/xml/docbook/xml-dtd-4.5')
		shutit.send('if [ ! -e /etc/xml/docbook ]; then xmlcatalog --noout --create /etc/xml/docbook; fi')
		shutit.send('xmlcatalog --noout --add "public" "-//OASIS//DTD DocBook XML V4.5//EN" "http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd" /etc/xml/docbook')
		shutit.send('xmlcatalog --noout --add "public" "-//OASIS//DTD DocBook XML CALS Table Model V4.5//EN" "file:///usr/share/xml/docbook/xml-dtd-4.5/calstblx.dtd" /etc/xml/docbook')
		shutit.send('xmlcatalog --noout --add "public" "-//OASIS//DTD XML Exchange Table Model 19990315//EN" "file:///usr/share/xml/docbook/xml-dtd-4.5/soextblx.dtd" /etc/xml/docbook')
		shutit.send('xmlcatalog --noout --add "public" "-//OASIS//ELEMENTS DocBook XML Information Pool V4.5//EN" "file:///usr/share/xml/docbook/xml-dtd-4.5/dbpoolx.mod" /etc/xml/docbook')
		shutit.send('xmlcatalog --noout --add "public" "-//OASIS//ELEMENTS DocBook XML Document Hierarchy V4.5//EN" "file:///usr/share/xml/docbook/xml-dtd-4.5/dbhierx.mod" /etc/xml/docbook')
		shutit.send('xmlcatalog --noout --add "public" "-//OASIS//ELEMENTS DocBook XML HTML Tables V4.5//EN" "file:///usr/share/xml/docbook/xml-dtd-4.5/htmltblx.mod" /etc/xml/docbook')
		shutit.send('xmlcatalog --noout --add "public" "-//OASIS//ENTITIES DocBook XML Notations V4.5//EN" "file:///usr/share/xml/docbook/xml-dtd-4.5/dbnotnx.mod" /etc/xml/docbook')
		shutit.send('xmlcatalog --noout --add "public" "-//OASIS//ENTITIES DocBook XML Character Entities V4.5//EN" "file:///usr/share/xml/docbook/xml-dtd-4.5/dbcentx.mod" /etc/xml/docbook')
		shutit.send('xmlcatalog --noout --add "public" "-//OASIS//ENTITIES DocBook XML Additional General Entities V4.5//EN" "file:///usr/share/xml/docbook/xml-dtd-4.5/dbgenent.mod" /etc/xml/docbook')
		shutit.send('xmlcatalog --noout --add "rewriteSystem" "http://www.oasis-open.org/docbook/xml/4.5" "file:///usr/share/xml/docbook/xml-dtd-4.5" /etc/xml/docbook')
		shutit.send('xmlcatalog --noout --add "rewriteURI" "http://www.oasis-open.org/docbook/xml/4.5" "file:///usr/share/xml/docbook/xml-dtd-4.5" /etc/xml/docbook')
		shutit.send('if [ ! -e /etc/xml/catalog ]; then xmlcatalog --noout --create /etc/xml/catalog; fi')
		shutit.send('xmlcatalog --noout --add "delegatePublic" "-//OASIS//ENTITIES DocBook XML" "file:///etc/xml/docbook" /etc/xml/catalog')
		shutit.send('xmlcatalog --noout --add "delegatePublic" "-//OASIS//DTD DocBook XML" "file:///etc/xml/docbook" /etc/xml/catalog')
		shutit.send('xmlcatalog --noout --add "delegateSystem" "http://www.oasis-open.org/docbook/" "file:///etc/xml/docbook" /etc/xml/catalog')
		shutit.send('xmlcatalog --noout --add "delegateURI" "http://www.oasis-open.org/docbook/" "file:///etc/xml/docbook" /etc/xml/catalog')
		shutit.run_script(r'''
			for DTDVERSION in 4.1.2 4.2 4.3 4.4
			do
			  xmlcatalog --noout --add "public" \
			    "-//OASIS//DTD DocBook XML V$DTDVERSION//EN" \
			    "http://www.oasis-open.org/docbook/xml/$DTDVERSION/docbookx.dtd" \
			    /etc/xml/docbook
			  xmlcatalog --noout --add "rewriteSystem" \
			    "http://www.oasis-open.org/docbook/xml/$DTDVERSION" \
			    "file:///usr/share/xml/docbook/xml-dtd-4.5" \
			    /etc/xml/docbook
			  xmlcatalog --noout --add "rewriteURI" \
			    "http://www.oasis-open.org/docbook/xml/$DTDVERSION" \
			    "file:///usr/share/xml/docbook/xml-dtd-4.5" \
			    /etc/xml/docbook
			  xmlcatalog --noout --add "delegateSystem" \
			    "http://www.oasis-open.org/docbook/xml/$DTDVERSION/" \
			    "file:///etc/xml/docbook" \
			    /etc/xml/catalog
			  xmlcatalog --noout --add "delegateURI" \
			    "http://www.oasis-open.org/docbook/xml/$DTDVERSION/" \
			    "file:///etc/xml/docbook" \
			    /etc/xml/catalog
			done''')
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
	return docbookxml(
		'shutit.tk.sd.docbookxml.docbookxml', 158844782.0112351235,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libxml2.libxml2','shutit.tk.sd.zip.zip']
	)

