#!/bin/bash
for d in setup apache_portable_runtime autoconf libffi python2 sqlite tcl zip automake apache_portable_runtime_util serf zlib libssl python_pip libxml2 libxslt lxml docbookxsl scons
do
	cd $d/bin
	echo $(date)
	echo $d BEGIN
	./build_and_push.sh > /tmp/shutitdistout 2>&1
	if [[ $? != 0 ]]
	then
		echo FAILED
	fi
	echo $(date)
	echo $d DONE
	cd -
done

