#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : deprecation
Version  : 2.1.0
Release  : 25
URL      : https://files.pythonhosted.org/packages/5a/d3/8ae2869247df154b64c1884d7346d412fed0c49df84db635aab2d1c40e62/deprecation-2.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5a/d3/8ae2869247df154b64c1884d7346d412fed0c49df84db635aab2d1c40e62/deprecation-2.1.0.tar.gz
Summary  : A library to handle automated deprecations
Group    : Development/Tools
License  : Apache-2.0
Requires: deprecation-license = %{version}-%{release}
Requires: deprecation-python = %{version}-%{release}
Requires: deprecation-python3 = %{version}-%{release}
Requires: packaging
BuildRequires : buildreq-distutils3
BuildRequires : packaging

%description
deprecation
===========
.. image:: https://readthedocs.org/projects/deprecation/badge/?version=latest
:target: http://deprecation.readthedocs.io/en/latest/
:alt: Documentation Status

%package license
Summary: license components for the deprecation package.
Group: Default

%description license
license components for the deprecation package.


%package python
Summary: python components for the deprecation package.
Group: Default
Requires: deprecation-python3 = %{version}-%{release}

%description python
python components for the deprecation package.


%package python3
Summary: python3 components for the deprecation package.
Group: Default
Requires: python3-core
Provides: pypi(deprecation)
Requires: pypi(packaging)

%description python3
python3 components for the deprecation package.


%prep
%setup -q -n deprecation-2.1.0
cd %{_builddir}/deprecation-2.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587407727
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecation
cp %{_builddir}/deprecation-2.1.0/LICENSE %{buildroot}/usr/share/package-licenses/deprecation/92170cdc034b2ff819323ff670d3b7266c8bffcd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecation/92170cdc034b2ff819323ff670d3b7266c8bffcd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
