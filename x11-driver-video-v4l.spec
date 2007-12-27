Name: x11-driver-video-v4l
Version: 0.1.1
Release: %mkrel 4
Summary: Xvideo extension port for video overlay
Group: Development/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-video-v4l-0.1.1@mandriva suggested on upstream
# Tag at git checkout 6260e7a8166cefb57c85d3e6aa3ac9f421e2a8b9
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-v4l  xorg/drivers/xf86-video-v4l
# cd xorg/drivers/xf86-video/v4l
# git-archive --format=tar --prefix=xf86-video-v4l-0.1.1/ xf86-video-v4l-0.1.1@mandriva | bzip2 -9 > xf86-video-v4l-0.1.1.tar.bz2
########################################################################
Source0: xf86-video-v4l-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-v4l-0.1.1@mandriva..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.1.5-4mdk
BuildRequires: x11-util-modular
# (tv): v4l need the extmod module
Requires: x11-server-common
Conflicts: x11-server < 1.4

%description
v4l is an Xorg driver for video4linux cards. It provides a Xvideo
extension port for video overlay.

%package devel
Summary: Development files for %{name}
Group: Development/X11
License: MIT

%description devel
Development files for %{name}

%prep
%setup -q -n xf86-video-v4l-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
# Create list of dependencies
x-check-deps.pl
for deps in *.deps; do
    install -D -m 644 $deps %{buildroot}/%{_datadir}/X11/mandriva/$deps
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/v4l_drv.so
%{_mandir}/man4/v4l.*

%files devel
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/*.la
%{_datadir}/X11/mandriva/*.deps
