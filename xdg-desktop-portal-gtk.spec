#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xdg-desktop-portal-gtk
Version  : 1.7.1
Release  : 10
URL      : https://github.com/flatpak/xdg-desktop-portal-gtk/releases/download/1.7.1/xdg-desktop-portal-gtk-1.7.1.tar.xz
Source0  : https://github.com/flatpak/xdg-desktop-portal-gtk/releases/download/1.7.1/xdg-desktop-portal-gtk-1.7.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: xdg-desktop-portal-gtk-data = %{version}-%{release}
Requires: xdg-desktop-portal-gtk-libexec = %{version}-%{release}
Requires: xdg-desktop-portal-gtk-license = %{version}-%{release}
Requires: xdg-desktop-portal-gtk-locales = %{version}-%{release}
Requires: xdg-desktop-portal-gtk-services = %{version}-%{release}
Requires: xdg-desktop-portal
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gtk+-unix-print-3.0)
BuildRequires : pkgconfig(gtk+-wayland-3.0)
BuildRequires : pkgconfig(gtk+-x11-3.0)
BuildRequires : pkgconfig(xdg-desktop-portal)
BuildRequires : sed
BuildRequires : xdg-desktop-portal

%description
No detailed description available

%package data
Summary: data components for the xdg-desktop-portal-gtk package.
Group: Data

%description data
data components for the xdg-desktop-portal-gtk package.


%package libexec
Summary: libexec components for the xdg-desktop-portal-gtk package.
Group: Default
Requires: xdg-desktop-portal-gtk-license = %{version}-%{release}

%description libexec
libexec components for the xdg-desktop-portal-gtk package.


%package license
Summary: license components for the xdg-desktop-portal-gtk package.
Group: Default

%description license
license components for the xdg-desktop-portal-gtk package.


%package locales
Summary: locales components for the xdg-desktop-portal-gtk package.
Group: Default

%description locales
locales components for the xdg-desktop-portal-gtk package.


%package services
Summary: services components for the xdg-desktop-portal-gtk package.
Group: Systemd services

%description services
services components for the xdg-desktop-portal-gtk package.


%prep
%setup -q -n xdg-desktop-portal-gtk-1.7.1
cd %{_builddir}/xdg-desktop-portal-gtk-1.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588216075
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1588216075
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-gtk
cp %{_builddir}/xdg-desktop-portal-gtk-1.7.1/COPYING %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-gtk/01a6b4bf79aca9b556822601186afab86e8c4fbf
%make_install
%find_lang xdg-desktop-portal-gtk

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/applications/xdg-desktop-portal-gtk.desktop
/usr/share/dbus-1/services/org.freedesktop.impl.portal.desktop.gtk.service
/usr/share/xdg-desktop-portal/portals/gtk.portal

%files libexec
%defattr(-,root,root,-)
/usr/libexec/xdg-desktop-portal-gtk

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xdg-desktop-portal-gtk/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/xdg-desktop-portal-gtk.service

%files locales -f xdg-desktop-portal-gtk.lang
%defattr(-,root,root,-)

