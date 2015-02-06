%define name XawM
%define version 1.5u
%define release  11

%define major 1
%define libname %mklibname %name %{major}
%define develname %mklibname -d %name

Summary:   Widget based on Xaw3d
Name:      %{name}
Version:   %{version}
Release:   %{release}
URL:       http://falconer.best.vwh.net/Widgets/#xawm
Source:    %{name}-%{version}.tar.bz2
Patch0:    XawM-1.5u-fix-linkage.patch
License:   MIT
Group:     System/Libraries
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xt)

%description
An Athena-compatible widget set with a modern look and feel.

%package -n %{libname}
Summary: Widget based on Xaw3d
Group: System/Libraries

%description -n %{libname}
An Athena-compatible widget set with a modern look and feel.

%package -n %{develname}
Summary:  Widget based on Xaw3d
Group:    Development/C
Requires: %{libname} = %{version}-%{release}
Provides: libXawM-devel = %{version}-%{release}
Provides: XawM-devel = %{version}-%{release}
Obsoletes: %{_lib}XawM1-devel < %{version}-%{release}

%description -n %{develname}
An Athena-compatible widget set with a modern look and feel.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog README* 
%{_libdir}/lib*.so.%{major}
%{_libdir}/lib*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/X11/XawM
%{_libdir}/lib*.*a
%{_libdir}/lib*.so


%changelog
* Sun Feb 21 2010 Funda Wang <fwang@mandriva.org> 1.5u-9mdv2010.1
+ Revision: 508948
- autoreconf
- add missing patch
- new devel package policy
- fix build

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.5u-5mdv2008.1
+ Revision: 136576
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - import XawM


* Fri May 19 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.5u-5mdk
- use %%mkrel
- fix buildrequires

* Tue Dec 07 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.5u-4mdk
- rebuild

* Sat Sep 13 2003 Stefan van der Eijk <stefan@eijk.nu> 1.5u-3mdk
- mklibname (rpmlint)
- renanme spec file (rpmlint)
- BuildRequires: XFree86-devel
- Requires: XFree86-devel --> for devel package (need the
  /usr/includeX11 symlink)
- Move files from /usr/include/X11 to /usr/X11R6/include/X11 to avoid
  clash with XFree86-devel installation (broken symlinks, etc)

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.5u-2mdk
- rebuild

* Tue Jan 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.5u-1mdk
- new & needed to update siag
