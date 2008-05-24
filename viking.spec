Summary:	GPS data editor and analyzer
Name:		viking
Version:	0.9.4
Release:	1
License:	GPLv2
Group:		X11/Applications
URL:		http://viking.sourceforge.net/
Source0:	http://dl.sourceforge.net/viking/%{name}-%{version}.tar.gz
# Source0-md5:	2bbd80435535a4be897ac56c8bf5f8ae
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	gettext
BuildRequires:	perl(XML::Parser)
BuildRequires:	gpsd-devel
BuildRequires:	gtk+2-devel >= 2.2.0
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
%{__make} DESTDIR=$RPM_BUILD_ROOT install
%find_lang %{name}
rm -f doc/Makefile*
rm -f doc/dev/Makefile*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO doc/
%attr(755,root,root) %{_bindir}/viking
%attr(755,root,root) %{_bindir}/viking-remote
