#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5A62D0CAB6264964 (reiter.christoph@gmail.com)
#
Name     : pycairo
Version  : 1.21.0
Release  : 58
URL      : https://github.com/pygobject/pycairo/releases/download/v1.21.0/pycairo-1.21.0.tar.gz
Source0  : https://github.com/pygobject/pycairo/releases/download/v1.21.0/pycairo-1.21.0.tar.gz
Source1  : https://github.com/pygobject/pycairo/releases/download/v1.21.0/pycairo-1.21.0.tar.gz.sig
Summary  : Python interface for cairo
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1-only MPL-1.1
Requires: pycairo-filemap = %{version}-%{release}
Requires: pycairo-lib = %{version}-%{release}
Requires: pycairo-license = %{version}-%{release}
Requires: pycairo-python = %{version}-%{release}
Requires: pycairo-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(cairo)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
Patch1: 0001-Move-pkgconfig-directory-to-usr-lib64-pkgconfig.patch

%description
.. image:: https://raw.githubusercontent.com/pygobject/pycairo/master/docs/images/pycairo.svg
:align: center
:width: 370px

%package dev
Summary: dev components for the pycairo package.
Group: Development
Requires: pycairo-lib = %{version}-%{release}
Provides: pycairo-devel = %{version}-%{release}
Requires: pycairo = %{version}-%{release}

%description dev
dev components for the pycairo package.


%package filemap
Summary: filemap components for the pycairo package.
Group: Default

%description filemap
filemap components for the pycairo package.


%package lib
Summary: lib components for the pycairo package.
Group: Libraries
Requires: pycairo-license = %{version}-%{release}
Requires: pycairo-filemap = %{version}-%{release}

%description lib
lib components for the pycairo package.


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
Requires: pycairo-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(pycairo)

%description python3
python3 components for the pycairo package.


%prep
%setup -q -n pycairo-1.21.0
cd %{_builddir}/pycairo-1.21.0
%patch1 -p1
pushd ..
cp -a pycairo-1.21.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666026835
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pycairo
cp %{_builddir}/pycairo-%{version}/COPYING-LGPL-2.1 %{buildroot}/usr/share/package-licenses/pycairo/7898de9d8a0026da533e44a786a17e435d7697f0 || :
cp %{_builddir}/pycairo-%{version}/COPYING-MPL-1.1 %{buildroot}/usr/share/package-licenses/pycairo/aba8d76d0af67d57da3c3c321caa59f3d242386b || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/pycairo/py3cairo.h
/usr/lib/python3.10/site-packages/cairo/include/py3cairo.h
/usr/lib64/pkgconfig/py3cairo.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pycairo

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pycairo/7898de9d8a0026da533e44a786a17e435d7697f0
/usr/share/package-licenses/pycairo/aba8d76d0af67d57da3c3c321caa59f3d242386b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
