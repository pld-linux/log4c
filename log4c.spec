Summary:	Library for flexible logging
Summary(pl.UTF-8):	Biblioteka do elastycznego logowania
Name:		log4c
Version:	1.2.4
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/log4c/%{name}-%{version}.tar.gz
# Source0-md5:	0d94919136e1d16b68427562e74cb3dd
Patch0:		%{name}-nolatex.patch
Patch1:		%{name}-doc.patch
Patch2:		%{name}-cxx.patch
Patch3:		%{name}-format.patch
URL:		http://log4c.sourceforge.net/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7
BuildRequires:	doxygen
BuildRequires:	expat-devel >= 1.95.1
BuildRequires:	graphviz
BuildRequires:	libtool >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for flexible logging.

%description -l pl.UTF-8
Biblioteka do elastycznego logowania.

%package devel
Summary:	Header files for log4c
Summary(pl.UTF-8):	Pliki nagłówkowe log4c
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development and header files for log4c.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki log4c.

%package static
Summary:	Static log4c library
Summary(pl.UTF-8):	Statyczna biblioteka log4c
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static log4c library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę log4c.

%package apidocs
Summary:	API documentation for log4c library
Summary(pl.UTF-8):	Dokumentacja API biblioteki log4c
Group:		Documentation

%description apidocs
API documentation for log4c library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki log4c.

%prep
%setup -q
%patch0
%patch1 -p1
%patch2
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal} -Iconfig
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

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblog4c.la

%{__rm} -r $RPM_BUILD_ROOT/removeit
%{__rm} -r $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README log4crc.sample
%attr(755,root,root) %{_libdir}/liblog4c.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblog4c.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/log4c-config
%attr(755,root,root) %{_libdir}/liblog4c.so
%{_includedir}/log4c
%{_includedir}/log4c.h
%{_pkgconfigdir}/log4c.pc
%{_mandir}/man1/log4c-config.1*
%{_mandir}/man3/log4c_*.3*
%{_aclocaldir}/log4c.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/liblog4c.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
