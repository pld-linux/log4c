Summary:	Library for flexible logging
Summary(pl):	Biblioteka do elastycznego logowania
Name:		log4c
Version:	1.0.10
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	db901a69a6da4f1974bf47105a9aac8a
Patch0:		%{name}-nolatex.patch
Patch1:		%{name}-destdir.patch
Patch2:		%{name}-doc.patch
URL:		http://log4cpp.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	expat-devel
BuildRequires:	graphviz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for flexible logging.

%description -l pl
Biblioteka do elastycznego logowania

%package devel
Summary:	Header files for log4c
Summary(pl):	Pliki nag³ówkowe log4c
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development and header files for log4c.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki log4c.

%package static
Summary:	Static log4c library
Summary(pl):	Statyczna biblioteka log4c
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static log4c library.

%description static -l pl
Ten pakiet zawiera statyczn± bibliotekê log4c.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%{__autoheader}
%configure
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
