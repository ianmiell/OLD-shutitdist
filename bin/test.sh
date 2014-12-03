#!/bin/bash
for d in setup tcl autoconf gperf icu sqlite which gmp lzo onigurama flex xmlto gettext automake libffi zlib apache_portable_runtime pkg_config openssl libssl zip python2 llvm asciidoc expat texinfo help2man libxml2 python_pip nettle tls libarchive libxslt docbookxsl apache_portable_runtime_util scons curl cmake serf subversion gmp nettle tls git libtool jq sthttpd curl cmake
do
	pushd ../$d/bin
	echo $(date)
	echo $d BEGIN
	./build_and_push.sh > /tmp/shutitdistout 2>&1
	if [[ $? != 0 ]]
	then
		echo FAILED
		exit 1
	fi
	echo $(date)
	echo $d DONE
	popd
done

