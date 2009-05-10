Summary:	GPS data editor and analyzer
Name:		viking
Version:	0.9.8
Release:	1
License:	GPLv2
Group:		X11/Applications
URL:		http://viking.sourceforge.net/
Source0:	http://dl.sourceforge.net/viking/%{name}-%{version}.tar.gz
# Source0-md5:	62c8cce4c755aba53edccea13284f7b8
Patch0:		%{name}-opencaching.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	gettext
BuildRequires:	gpsd-devel
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Viking is a free/open source program to manage GPS data. You can
import and plot tracks and waypoints, show Terraserver maps under it,
add coordinate lines, make new tracks and waypoints, hide different
things, etc. It is written in C with the GTK+ 2.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install iconsdir=%{_pixmapsdir}

%find_lang %{name}
rm -f doc/Makefile*
rm -f doc/dev/Makefile*

%check
make test

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO doc/
%attr(755,root,root) %{_bindir}/viking
%attr(755,root,root) %{_bindir}/viking-remote
%attr(755,root,root) %{_bindir}/vik_ocget
%{_desktopdir}/viking.desktop
%{_pixmapsdir}/viking.png
