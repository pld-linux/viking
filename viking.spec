Summary:	GPS data editor and analyzer
Name:		viking
Version:	1.6.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/viking/%{name}-%{version}.tar.bz2
# Source0-md5:	e79d8a092ef12a01975d4b92d30d9eb1
URL:		http://viking.sourceforge.net/
BuildRequires:	curl-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	expat-devel
BuildRequires:	gexiv2-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gpsd-devel
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-progs
BuildRequires:	mapnik-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout	-flto

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

%find_lang %{name} --with-gnome --with-omf

%check
make test

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO 
%attr(755,root,root) %{_bindir}/viking
%{_desktopdir}/viking.desktop
%{_pixmapsdir}/viking.png
%{_datadir}/viking
