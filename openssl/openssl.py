"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class openssl(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/openssl')
		shutit.send('cd /tmp/build/openssl')
		shutit.send('curl -L http://www.openssl.org/source/openssl-1.0.1i.tar.gz | tar -zxf -')
		shutit.send('cd openssl-*')
		shutit.send('curl http://www.linuxfromscratch.org/patches/blfs/7.6/openssl-1.0.1i-fix_parallel_build-1.patch | patch -Np1 -i -')
		shutit.send('./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib shared zlib-dynamic')
		shutit.send('make')
		shutit.send('make MANDIR=/usr/share/man MANSUFFIX=ssl install')
		shutit.send('install -dv -m755 /usr/share/doc/openssl-1.0.1i')
		shutit.send('cp -vfr doc/* /usr/share/doc/openssl-1.0.1i')
		shutit.send_host_file('/usr/bin/make-cert.pl','context/make-cert.pl')
		shutit.send('chmod +x /usr/bin/make-cert.pl')
		shutit.send_host_file('/usr/bin/make-ca.sh','context/make-ca.sh')
		shutit.send('chmod +x /usr/bin/make-ca.sh')
		shutit.send_host_file('/usr/bin/remove-expired-certs.sh','context/remove-expired-certs.sh')
		shutit.send('chmod +x /usr/bin/remove-expired-certs.sh')
		shutit.send('rm -f certdata.txt')
		shutit.send('curl -L http://anduin.linuxfromscratch.org/sources/other/certdata.txt > certdata.txt')
		shutit.send('make-ca.sh')
		shutit.send('remove-expired-certs.sh certs')
		shutit.send('install -d /etc/ssl/certs')
		shutit.send('cp -v certs/*.pem /etc/ssl/certs')
		shutit.send('c_rehash')
		shutit.send('install BLFS-ca-bundle*.crt /etc/ssl/ca-bundle.crt')
		shutit.send('ln -sfv ../ca-bundle.crt /etc/ssl/certs/ca-certificates.crt')
		shutit.send('rm -r certs BLFS-ca-bundle*')
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
	return openssl(
		'shutit.tk.sd.openssl.openssl', 158844782.001012125,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.zlib.zlib']
	)

