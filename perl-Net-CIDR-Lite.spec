#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-CIDR-Lite
Version  : 0.22
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/S/ST/STIGTSP/Net-CIDR-Lite-0.22.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/ST/STIGTSP/Net-CIDR-Lite-0.22.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-cidr-lite-perl/libnet-cidr-lite-perl_0.21-2.debian.tar.xz
Summary  : Perl extension for merging IPv4 or IPv6 CIDR addresses
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Net-CIDR-Lite-license = %{version}-%{release}
Requires: perl-Net-CIDR-Lite-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Net/CIDR/Lite version 0.22
==========================
INSTALLATION
To install this module type the following:

%package dev
Summary: dev components for the perl-Net-CIDR-Lite package.
Group: Development
Provides: perl-Net-CIDR-Lite-devel = %{version}-%{release}
Requires: perl-Net-CIDR-Lite = %{version}-%{release}

%description dev
dev components for the perl-Net-CIDR-Lite package.


%package license
Summary: license components for the perl-Net-CIDR-Lite package.
Group: Default

%description license
license components for the perl-Net-CIDR-Lite package.


%package perl
Summary: perl components for the perl-Net-CIDR-Lite package.
Group: Default
Requires: perl-Net-CIDR-Lite = %{version}-%{release}

%description perl
perl components for the perl-Net-CIDR-Lite package.


%prep
%setup -q -n Net-CIDR-Lite-0.22
cd %{_builddir}
tar xf %{_sourcedir}/libnet-cidr-lite-perl_0.21-2.debian.tar.xz
cd %{_builddir}/Net-CIDR-Lite-0.22
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Net-CIDR-Lite-0.22/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-CIDR-Lite
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Net-CIDR-Lite/46339a1166e8b5a59b054ebdbf37fe126a2bfeb4
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::CIDR::Lite.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-CIDR-Lite/46339a1166e8b5a59b054ebdbf37fe126a2bfeb4

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Net/CIDR/Lite.pm
