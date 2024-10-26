#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v12
# autospec commit: 381dfd8
#
# Source0 file verified with key 0x5A62D0CAB6264964 (reiter.christoph@gmail.com)
#
Name     : pycairo
Version  : 1.26.1
Release  : 75
URL      : https://github.com/pygobject/pycairo/releases/download/v1.26.1/pycairo-1.26.1.tar.gz
Source0  : https://github.com/pygobject/pycairo/releases/download/v1.26.1/pycairo-1.26.1.tar.gz
Source1  : https://github.com/pygobject/pycairo/releases/download/v1.26.1/pycairo-1.26.1.tar.gz.sig
Source2  : 5A62D0CAB6264964.pkey
Summary  : Python interface for cairo
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1-only MPL-1.1
Requires: pycairo-license = %{version}-%{release}
Requires: pycairo-python = %{version}-%{release}
Requires: pycairo-python3 = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : cairo-dev
BuildRequires : gnupg
BuildRequires : pkgconfig(cairo)
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Move-pkgconfig-directory-to-usr-lib64-pkgconfig.patch

%description
.. image:: https://raw.githubusercontent.com/pygobject/pycairo/main/docs/images/pycairo.svg
:align: center
:width: 370px

%package dev
Summary: dev components for the pycairo package.
Group: Development
Provides: pycairo-devel = %{version}-%{release}
Requires: pycairo = %{version}-%{release}

%description dev
dev components for the pycairo package.


%package license
Summary: license components for the pycairo package.
Group: Default

%description license
license components for the pycairo package.


%package python
Summary: python components for the pycairo package.
Group: Default
Requires: pycairo-python3 = %{version}-%{release}

%description python
python components for the pycairo package.


%package python3
Summary: python3 components for the pycairo package.
Group: Default
Requires: python3-core
Provides: pypi(pycairo)

%description python3
python3 components for the pycairo package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 5A62D0CAB6264964' gpg.status
%setup -q -n pycairo-1.26.1
cd %{_builddir}/pycairo-1.26.1
%patch -P 1 -p1
pushd ..
cp -a pycairo-1.26.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718983597
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/pycairo
cp %{_builddir}/pycairo-%{version}/COPYING-LGPL-2.1 %{buildroot}/usr/share/package-licenses/pycairo/7898de9d8a0026da533e44a786a17e435d7697f0 || :
cp %{_builddir}/pycairo-%{version}/COPYING-MPL-1.1 %{buildroot}/usr/share/package-licenses/pycairo/aba8d76d0af67d57da3c3c321caa59f3d242386b || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/pycairo/py3cairo.h
/usr/lib/python3.12/site-packages/cairo/include/py3cairo.h
/usr/lib64/pkgconfig/py3cairo.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pycairo/7898de9d8a0026da533e44a786a17e435d7697f0
/usr/share/package-licenses/pycairo/aba8d76d0af67d57da3c3c321caa59f3d242386b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
