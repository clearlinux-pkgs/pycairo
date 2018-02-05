#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5A62D0CAB6264964 (reiter.christoph@gmail.com)
#
Name     : pycairo
Version  : 1.16.0
Release  : 4
URL      : https://github.com/pygobject/pycairo/releases/download/v1.16.0/pycairo-1.16.0.tar.gz
Source0  : https://github.com/pygobject/pycairo/releases/download/v1.16.0/pycairo-1.16.0.tar.gz
Source99 : https://github.com/pygobject/pycairo/releases/download/v1.16.0/pycairo-1.16.0.tar.gz.sig
Summary  : Python interface for cairo
Group    : Development/Tools
License  : LGPL-2.1 MPL-1.1
Requires: pycairo-legacypython
Requires: pycairo-python3
Requires: pycairo-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(cairo)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: 0001-Move-pkgconfig-directory-to-usr-lib64-pkgconfig.patch

%description
.. image:: https://cdn.rawgit.com/pygobject/pycairo/master/docs/images/pycairo.svg
:align: center
:width: 370px

%package dev
Summary: dev components for the pycairo package.
Group: Development
Provides: pycairo-devel

%description dev
dev components for the pycairo package.


%package legacypython
Summary: legacypython components for the pycairo package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pycairo package.


%package python
Summary: python components for the pycairo package.
Group: Default
Requires: pycairo-legacypython
Requires: pycairo-python3

%description python
python components for the pycairo package.


%package python3
Summary: python3 components for the pycairo package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pycairo package.


%prep
%setup -q -n pycairo-1.16.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517856398
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1517856398
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/pycairo/py3cairo.h
/usr/include/pycairo/pycairo.h
/usr/lib/python2.7/site-packages/cairo/include/pycairo.h
/usr/lib/python3.6/site-packages/cairo/include/py3cairo.h
/usr/lib64/pkgconfig/py3cairo.pc
/usr/lib64/pkgconfig/pycairo.pc

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
