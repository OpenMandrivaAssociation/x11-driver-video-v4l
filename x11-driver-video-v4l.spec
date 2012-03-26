Name: x11-driver-video-v4l
Version: 0.2.0
Release: 12
Summary: Xvideo extension port for video overlay
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-v4l-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
# (tv): v4l need the extmod module
Requires: x11-server-common
Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)
Conflicts: x11-server < 1.4

%description
v4l is an Xorg driver for video4linux cards. It provides a Xvideo
extension port for video overlay.

%prep
%setup -qn xf86-video-v4l-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/v4l_drv.so
%{_mandir}/man4/v4l.*

