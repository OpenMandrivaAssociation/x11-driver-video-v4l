Name: x11-driver-video-v4l
Version: 0.1.1
Release: %mkrel 2
Summary: Xvideo extension port for video overlay
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-v4l-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
# (tv): v4l need the extmod module
Requires: x11-server-common
Conflicts: xorg-x11-server < 7.0

%description
v4l is an Xorg driver for video4linux cards. It provides a Xvideo
extension port for video overlay.

%prep
%setup -q -n xf86-video-v4l-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/v4l_drv.la
%{_libdir}/xorg/modules/drivers/v4l_drv.so
%{_mandir}/man4/v4l.*
