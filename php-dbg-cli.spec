Summary:	dbg-cli - a free front-end for dbg PHP debbuger
Summary(pl):	dbg-cli - wolnodostêpny frontend dla debuggera PHP dbg
Name:		php-dbg-cli
Version:	2.13.1
Release:	0.1
License:	The DBG License Version 3.0
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/dbg2/dbg-cli-%{version}-src.tar.gz
# Source0-md5:	3cb0a8bc2a03a0815ed24b2da602e72f
Patch0:		%{name}-pcre.patch
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

%description
DBG is a a full-featured PHP debugger, an interactive tool that helps
you debugging PHP scripts. It works on a production and/or development
WEB server and allows you debug your scripts locally or remotely, from
an IDE or console.

This package contains DBG CLI - a free front-end for dbg.

%description -l pl
DBG to w pe³ni funkcjonalny debugger dla PHP - interaktywne narzêdzie
pomagaj±ce przy diagnostyce skryptów w PHP. Dzia³a zarówno na
produkcyjnym jak i rozwojowym serwerze WWW, pozwala na ¶ledzenie
skryptów lokalnie jak i zdalnie, z poziomu IDE lub konsoli.

Ten pakiet zawiera DBG CLI - wolnodostêpny frontend dla dbg.

%prep
%setup -q -n dbg-cli-%{version}-src
%patch0 -p1
rm -rf pcre

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
