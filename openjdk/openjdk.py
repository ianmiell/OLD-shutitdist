"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class openjdk(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
#http://icedtea.classpath.org/download/source/icedtea-2.5.2.tar.xz | xz -d | tar -xf -
#http://www.linuxfromscratch.org/patches/blfs/7.6/icedtea-2.5.2-add_cacerts-1.patch
#http://www.linuxfromscratch.org/patches/blfs/7.6/icedtea-2.5.2-fixed_paths-1.patch
#http://www.linuxfromscratch.org/patches/blfs/7.6/icedtea-2.5.2-fix_new_giflib-1.patch
#http://www.linuxfromscratch.org/patches/blfs/7.6/icedtea-2.5.2-fix_tests-1.patch
#https://github.com/downloads/mozilla/rhino/rhino1_7R4.zip
#http://icedtea.classpath.org/download/source/icedtea-web-1.5.1.tar.gz
#Required Dependencies
#An existing binary ( Java-1.7.0.65 or an earlier built version of this package), alsa-lib-1.0.28, apache-ant-1.9.4, Certificate Authority Certificates, cpio-2.11, Cups-1.7.5, GTK+-2.24.24, giflib-5.1.0, UnZip-6.0, Wget-1.15, Which-2.20, Xorg Libraries, and Zip-3.0 


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
	return openjdk(
		'shutit.tk.sd.openjdk.openjdk', 158844782.00,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.setup.setup']
	)

