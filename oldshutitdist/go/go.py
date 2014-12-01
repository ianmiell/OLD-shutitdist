"""ShutIt module. See http://shutit.tk/
"""
#Copyright (C) 2014 OpenBet Limited
#
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is furnished
#to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from shutit_module import ShutItModule

class go(ShutItModule):

	def is_installed(self,shutit):
		return False

	def build(self,shutit):
		#shutit.install('golang')
		#shutit.install('mercurial')
		#shutit.install('gcc')
		#shutit.install('patch')
		#shutit.install('git')
		#shutit.add_to_bashrc('export PATH=$PATH:/opt/go/go/bin')
		#shutit.send('mkdir -p /opt/go')
		#shutit.send('hg clone -u release https://code.google.com/p/go')
		#shutit.send('pushd go/src')
		#shutit.send('./all.bash')
		#shutit.send('popd')
		shutit.send('wget https://storage.googleapis.com/golang/go' + shutit.cfg[self.module_id]['version'] + '.src.tar.gz')
		shutit.send('tar -zxf go' + shutit.cfg[self.module_id]['version'] + '.src.tar.gz')
		shutit.send('cd go/src/')
		shutit.send('GOROOT_FINAL=/usr ./make.bash')
		shutit.send('mv go /usr/bin')
		shutit.send('mv gofmt /usr/bin')
		return True

	def get_config(self,shutit):
		shutit.get_config(self.module_id,'version','1.3.3')
		return True

	#def check_ready(self,shutit):
	#    return True
	
	#def start(self,shutit):
	#    return True

	#def stop(self,shutit):
	#    return True

	def finalize(self,shutit):
		shutit.send('rm -rf /go')
		return True

	#def remove(self,shutit):
	#    return True

	#def test(self,shutit):
	#    return True

def module():
	return go(
		'shutit.tk.sd.go.go', 0.1346356,
		description='Go language setup (direct from source)',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.make.make']
	)

