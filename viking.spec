#
# TODO:
#	- real-time GPS tracking is disabled, as it doesn't build with current
#	gpsd-devel. It should be re-enabled after fixed.
#
Summary:	GPS data editor and analyzer
Name:		viking
Version:	1.2.2
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/viking/%{name}-%{version}.tar.gz
# Source0-md5:	460121f135ddc499bb4e51e61fa7fba7
Patch0:		%{name}-opencaching.patch
URL:		http://viking.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	expat-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
#BuildRequires:	gpsd-devel
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-progs
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Viking is a free/open source program to manage GPS data. You can
import and plot tracks and waypoints, show Terraserver maps under it,
add coordinate lines, make new tracks and waypoints, hide different
things, etc. It is written in C with the GTK+ 2.

%prep
%setup -q
%patch0 -p1

# workaround to make automake happy
install -d doc/reference
touch doc/reference/Makefile.in

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-realtime-gps-tracking
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install iconsdir=%{_pixmapsdir}

# copy before removing Makefiles so --short-circuit -bi will work
rm -rf dist-doc
cp -a doc dist-doc
rm -f dist-doc/Makefile*
rm -f dist-doc/*/Makefile*

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
%doc AUTHORS ChangeLog COPYING NEWS README TODO dist-doc/*
%attr(755,root,root) %{_bindir}/viking
%attr(755,root,root) %{_bindir}/viking-remote
%attr(755,root,root) %{_bindir}/vik_ocget
%{_desktopdir}/viking.desktop
%{_pixmapsdir}/viking.png
