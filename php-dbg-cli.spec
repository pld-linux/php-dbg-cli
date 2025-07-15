#
# TODO:
#		command.cpp:761: warning: overflow in implicit constant conversion
#		command.cpp:768: warning: overflow in implicit constant conversion
#		signed overflow is an undefined bahaviour and gcc optimizer
#		can produce random code ;)
#
#		-Wl,--as-needed breaks ./configure.
#
Summary:	dbg-cli - a free front-end for dbg PHP debbuger
Summary(pl.UTF-8):	dbg-cli - wolnodostępny frontend dla debuggera PHP dbg
Name:		php-dbg-cli
Version:	2.15.5
Release:	0.1
License:	The DBG License Version 3.0
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/dbg2/dbg-cli-%{version}-src.tar.gz
# Source0-md5:	10524eaf90dd177c709deb981419fcf4
Patch0:		%{name}-syslibs.patch
URL:		http://dd.cron.ru/dbg/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pcre-devel
BuildRequires:	readline-devel
Obsoletes:	dbg-cli
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# see TODO
%define		filterout_ld -Wl,--as-needed

%description
DBG is a a full-featured PHP debugger, an interactive tool that helps
you debugging PHP scripts. It works on a production and/or development
WEB server and allows you debug your scripts locally or remotely, from
an IDE or console.

This package contains DBG CLI - a free front-end for dbg.

%description -l pl.UTF-8
DBG to w pełni funkcjonalny debugger dla PHP - interaktywne narzędzie
pomagające przy diagnostyce skryptów w PHP. Działa zarówno na
produkcyjnym jak i rozwojowym serwerze WWW, pozwala na śledzenie
skryptów lokalnie jak i zdalnie, z poziomu IDE lub konsoli.

Ten pakiet zawiera DBG CLI - wolnodostępny frontend dla dbg.

%prep
%setup -q -n dbg-cli-%{version}-src
%patch -P0 -p1
rm -rf pcre getopt

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# nothing needs those
rm -rf $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING AUTHORS README
%attr(755,root,root) %{_bindir}/dbg-cli
