#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libiscsi
Version  : 1.19.0
Release  : 8
URL      : https://github.com/sahlberg/libiscsi/archive/1.19.0/libiscsi-1.19.0.tar.gz
Source0  : https://github.com/sahlberg/libiscsi/archive/1.19.0/libiscsi-1.19.0.tar.gz
Summary  : iSCSI initiator library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libiscsi-bin = %{version}-%{release}
Requires: libiscsi-lib = %{version}-%{release}
Requires: libiscsi-license = %{version}-%{release}
Requires: libiscsi-man = %{version}-%{release}
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev

%description
Libiscsi is a client-side library to implement the iSCSI protocol that can be used
to access the resources of an iSCSI target.

%package bin
Summary: bin components for the libiscsi package.
Group: Binaries
Requires: libiscsi-license = %{version}-%{release}

%description bin
bin components for the libiscsi package.


%package dev
Summary: dev components for the libiscsi package.
Group: Development
Requires: libiscsi-lib = %{version}-%{release}
Requires: libiscsi-bin = %{version}-%{release}
Provides: libiscsi-devel = %{version}-%{release}
Requires: libiscsi = %{version}-%{release}

%description dev
dev components for the libiscsi package.


%package lib
Summary: lib components for the libiscsi package.
Group: Libraries
Requires: libiscsi-license = %{version}-%{release}

%description lib
lib components for the libiscsi package.


%package license
Summary: license components for the libiscsi package.
Group: Default

%description license
license components for the libiscsi package.


%package man
Summary: man components for the libiscsi package.
Group: Default

%description man
man components for the libiscsi package.


%prep
%setup -q -n libiscsi-1.19.0
cd %{_builddir}/libiscsi-1.19.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604359188
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604359188
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libiscsi
cp %{_builddir}/libiscsi-1.19.0/COPYING %{buildroot}/usr/share/package-licenses/libiscsi/f12cd6fb8d937bce8255817b96793d0d1ea6f997
cp %{_builddir}/libiscsi-1.19.0/LICENCE-GPL-2.txt %{buildroot}/usr/share/package-licenses/libiscsi/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/libiscsi-1.19.0/LICENCE-LGPL-2.1.txt %{buildroot}/usr/share/package-licenses/libiscsi/01a6b4bf79aca9b556822601186afab86e8c4fbf
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/bin/ld_iscsi.so

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/iscsi-inq
/usr/bin/iscsi-ls
/usr/bin/iscsi-perf
/usr/bin/iscsi-readcapacity16
/usr/bin/iscsi-swp

%files dev
%defattr(-,root,root,-)
/usr/include/iscsi/iscsi.h
/usr/include/iscsi/scsi-lowlevel.h
/usr/lib64/libiscsi.so
/usr/lib64/pkgconfig/libiscsi.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libiscsi.so.9
/usr/lib64/libiscsi.so.9.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libiscsi/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/libiscsi/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/libiscsi/f12cd6fb8d937bce8255817b96793d0d1ea6f997

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/iscsi-inq.1
/usr/share/man/man1/iscsi-ls.1
/usr/share/man/man1/iscsi-swp.1
/usr/share/man/man1/iscsi-test-cu.1
