#!/bin/bash
if [[ $1 = '' ]]
then
	start="setup"
	started="1"
else
	start="$1"
	started="0"
fi
pushd ..
find . | grep .cnf$ | xargs chmod 0600
popd

#cat test.sh | grep git | tr ' ' '\n' | sort | grep -vw for | grep -vw d | grep -vw in > ../sortedtest
#ls -1 | grep -vw bin | grep -vw [A-Z] | sort > sorteddirs
#meld sorteddirs sortedtest


# Just the edges of the graph
#for d in setup yacc docbook_utils docbook_sgml_dtd iproute2 less procps_ng libidn gperf inetutils groff rsync linuxbrew kona sthttpd pango jq berkeleydb
for d in setup glib_config bzip2 tcl sharutils autoconf gperf icu sqlite which gmp lzo onigurama flex xmlto gettext automake libffi libidn texinfo util_macros expat zlib apache_portable_runtime pkg_config procps_ng openjade cpio zip python2 wget ncurses readline llvm asciidoc help2man libxml2 python_pip nettle tls libarchive libxslt docbookxml docbookxsl apache_portable_runtime_util scons cmake serf subversion git libtool jq sthttpd kona go xcb_proto libxau linuxbrew libpng libxcb glib harfbuzz rsync gawk sgml_common bison groff docbook vim lxml inetutils yacc iproute2 less giflib sudo x7proto alsa_lib freetype freetype2 desktop_file_utils fontconfig opensp docbook_dsssl docbook_sgml_dtd docbook_utils xorg_libs atk cups nasm libjpeg libtiff gdk_pixbuf pixman cairo pango gtk2 lcms java_binary ant junit findutils nspr nss openjdk berkeleydb apache erlang
# TODO: cyrus_sasl go
do
	if [[ $started = "0" ]]
	then
		if [[ $start = $d ]]
		then
			started="1"
		else
			continue
		fi
	fi
	pushd ../$d/bin
	echo "BEGIN $d $(date)" >> /tmp/shutitdistout
	./build_and_push.sh >> /tmp/shutitdistout
	if [[ $? != 0 ]]
	then
		echo "FAILED $d" >> /tmp/shutitdistout
		exit 1
	fi
	echo "DONE $d $(date)" >> /tmp/shutitdistout
	popd
done

