"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class apache(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('curl -L http://archive.apache.org/dist/httpd/httpd-2.4.10.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd httpd*')
		shutit.send('groupadd -g 25 apache')
		shutit.send('useradd -c "Apache Server" -d /srv/www -g apache -s /bin/false -u 25 apache')
		shutit.send('curl -L http://www.linuxfromscratch.org/patches/blfs/svn/httpd-2.4.10-blfs_layout-1.patch | patch -Np1 -i -')
		shutit.send('''sed '/dir.*CFG_PREFIX/s@^@#@' -i support/apxs.in''')
		shutit.send('./configure --enable-authnz-fcgi --enable-layout=BLFS --enable-mods-shared="all cgi" --enable-mpms-shared=all --enable-suexec=shared --with-apr=/usr/bin/apr-1-config --with-apr-util=/usr/bin/apu-1-config --with-suexec-bin=/usr/lib/httpd/suexec --with-suexec-caller=apache --with-suexec-docroot=/srv/www --with-suexec-logfile=/var/log/httpd/suexec.log --with-suexec-uidmin=100 --with-suexec-userdir=public_html')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('mv -v /usr/sbin/suexec /usr/lib/httpd/suexec')
		shutit.send('chgrp apache /usr/lib/httpd/suexec')
		shutit.send('chmod 4754 /usr/lib/httpd/suexec')
		shutit.send('chown -v -R apache:apache /srv/www')
# TODO (Apr-Util-1.5.4 needs to be installed with ldap suport
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
	return apache(
		'shutit.tk.sd.apache.apache', 158844782.007215135325,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.setup.setup','shutit.tk.sd.apache_portable_runtime_util.apache_portable_runtime_util','shutit.tk.sd.pcre.pcre','shutit.tk.libxml2.libml2']
	)

