Summary:	Library for flexible logging
Summary(pl.UTF-8):   Biblioteka do elastycznego logowania
Name:		log4c
Version:	1.0.12
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/log4c/%{name}-%{version}.tar.gz
# Source0-md5:	334d38ed163b26b1be48364b445ad170
Patch0:		%{name}-nolatex.patch
Patch1:		%{name}-doc.patch
URL:		http://log4cpp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	expat-devel
BuildRequires:	graphviz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for flexible logging.

%description -l pl.UTF-8
Biblioteka do elastycznego logowania.

%package devel
Summary:	Header files for log4c
Summary(pl.UTF-8):   Pliki nagłówkowe log4c
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development and header files for log4c.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki log4c.

%package static
Summary:	Static log4c library
Summary(pl.UTF-8):   Statyczna biblioteka log4c
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static log4c library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę log4c.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-doc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install  \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=/removeit

rm -rf $RPM_BUILD_ROOT/removeit
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README log4crc.sample
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_bindir}/log4c-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
