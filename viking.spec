Summary:	GPS data editor and analyzer
Name:		viking
Version:	0.9.5
Release:	1
License:	GPLv2
Group:		X11/Applications
URL:		http://viking.sourceforge.net/
Source0:	http://dl.sourceforge.net/viking/%{name}-%{version}.tar.gz
# Source0-md5:	b4daa3e395a5dbc156b1ab5f092e4009
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	gettext
BuildRequires:	gpsd-devel
BuildRequires:	gtk+2-devel >= 2.2.0
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

%build
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
[ ! -x %{_bindir}/update-desktop-database ] || %{_bindir}/update-desktop-database >/dev/null 2>&1 ||:

%postun
[ ! -x %{_bindir}/update-desktop-database ] || %{_bindir}/update-desktop-database >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO doc/
%attr(755,root,root) %{_bindir}/viking
%attr(755,root,root) %{_bindir}/viking-remote
%{_desktopdir}/viking.desktop
%{_pixmapsdir}/viking_icon.png
