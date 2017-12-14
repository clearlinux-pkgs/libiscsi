#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libiscsi
Version  : 1.18.0
Release  : 1
URL      : https://github.com/sahlberg/libiscsi/archive/1.18.0.tar.gz
Source0  : https://github.com/sahlberg/libiscsi/archive/1.18.0.tar.gz
Summary  : iSCSI initiator library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libiscsi-bin
Requires: libiscsi-lib
Requires: libiscsi-doc

%description
Libiscsi is a client-side library to implement the iSCSI protocol that can be used
to access the resources of an iSCSI target.

%package bin
Summary: bin components for the libiscsi package.
Group: Binaries

%description bin
bin components for the libiscsi package.


%package dev
Summary: dev components for the libiscsi package.
Group: Development
Requires: libiscsi-lib
Requires: libiscsi-bin
Provides: libiscsi-devel

%description dev
dev components for the libiscsi package.


%package doc
Summary: doc components for the libiscsi package.
Group: Documentation

%description doc
doc components for the libiscsi package.


%package lib
Summary: lib components for the libiscsi package.
Group: Libraries

%description lib
lib components for the libiscsi package.


%prep
%setup -q -n libiscsi-1.18.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513274100
%autogen --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1513274100
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/iscsi-inq
/usr/bin/iscsi-ls
/usr/bin/iscsi-perf
/usr/bin/iscsi-readcapacity16
/usr/bin/iscsi-swp
/usr/bin/ld_iscsi.so

%files dev
%defattr(-,root,root,-)
/usr/include/iscsi/iscsi.h
/usr/include/iscsi/scsi-lowlevel.h
/usr/lib64/libiscsi.so
/usr/lib64/pkgconfig/libiscsi.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libiscsi.so.8
/usr/lib64/libiscsi.so.8.0.0
