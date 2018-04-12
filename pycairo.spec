#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5A62D0CAB6264964 (reiter.christoph@gmail.com)
#
Name     : pycairo
Version  : 1.16.3
Release  : 12
URL      : https://github.com/pygobject/pycairo/releases/download/v1.16.3/pycairo-1.16.3.tar.gz
Source0  : https://github.com/pygobject/pycairo/releases/download/v1.16.3/pycairo-1.16.3.tar.gz
Source99 : https://github.com/pygobject/pycairo/releases/download/v1.16.3/pycairo-1.16.3.tar.gz.sig
Summary  : Python interface for cairo
Group    : Development/Tools
License  : LGPL-2.1 MPL-1.1
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


%package python
Summary: python components for the pycairo package.
Group: Default
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
%setup -q -n pycairo-1.16.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523550619
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/pycairo/py3cairo.h
/usr/lib/python3.6/site-packages/cairo/include/py3cairo.h
/usr/lib64/pkgconfig/py3cairo.pc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
