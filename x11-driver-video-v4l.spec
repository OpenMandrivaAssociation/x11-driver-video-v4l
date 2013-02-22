Name:		x11-driver-video-v4l
Version:	0.2.0
Release:	14
Summary:	Xvideo extension port for video overlay
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-v4l-%{version}.tar.bz2
Patch0:		xf86-video-v4l-0.2.0-automake1.13-fix.patch
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	pkgconfig(xorg-server) >= 1.13
BuildRequires:	x11-util-macros >= 1.0.1
# (tv): v4l need the extmod module
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
Conflicts:	x11-server < 1.4

%description
v4l is an Xorg driver for video4linux cards. It provides a Xvideo
extension port for video overlay.

%prep
%setup -qn xf86-video-v4l-%{version}
%patch0 -p1 -b .am113~
autoreconf -fiv

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/v4l_drv.so
%{_mandir}/man4/v4l.*
