Name: x11-driver-video-v4l
Version: 0.2.0
Release: 12
Summary: Xvideo extension port for video overlay
Group: System/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-v4l-%{version}.tar.bz2
License: MIT
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
# (tv): v4l need the extmod module
Requires: x11-server-common
Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)
Conflicts: x11-server < 1.4

%description
v4l is an Xorg driver for video4linux cards. It provides a Xvideo
extension port for video overlay.

%prep
%setup -q -n xf86-video-v4l-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/v4l_drv.so
%{_mandir}/man4/v4l.*


%changelog
* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.2.0-9mdv2011.0
+ Revision: 683555
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-8
+ Revision: 671184
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 0.2.0-7mdv2011.0
+ Revision: 595714
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 0.2.0-6mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Nov 10 2009 Thierry Vignaud <tv@mandriva.org> 0.2.0-5mdv2010.1
+ Revision: 464345
- rebuild for new xserver

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 0.2.0-4mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

  + Thierry Vignaud <tv@mandriva.org>
    - fix group

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 0.2.0-3mdv2009.1
+ Revision: 308179
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.2.0-2mdv2009.0
+ Revision: 265985
- rebuild early 2009.0 package (before pixel changes)

* Mon May 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.2.0-1mdv2009.0
+ Revision: 206274
- Update to upstream version 0.2.0.

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.1.1-6mdv2008.1
+ Revision: 166156
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.1.1-5mdv2008.1
+ Revision: 156626
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.1.1-4mdv2008.1
+ Revision: 154787
- Updated BuildRequires and resubmit package.
- rm -f %%{buildroot}/%%{_libdir}/xorg/modules/drivers/*.la
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-video-v4l-0.1.1@mandriva suggested on upstream
  Tag at git checkout 6260e7a8166cefb57c85d3e6aa3ac9f421e2a8b9
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 11 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.1.1-3mdv2008.1
+ Revision: 97219
- new release (to build against new x11-server)
- minor spec cleanup

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-2mdv2008.0
+ Revision: 75824
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


* Mon Jun 05 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-06-05 21:11:32 (36659)
- new upstream release

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 21:50:58 (31394)
- Requires x11-server-common since v4l need the extmod module

* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 21:50:32 (31393)
- fill in description & summary

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

