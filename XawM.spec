%define name XawM
%define version 1.5u
%define release %mkrel 9

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
BuildRequires: libx11-devel
BuildRequires: libxext-devel
BuildRequires: libxmu-devel
BuildRequires: libxt-devel
BuildRoot: %{_tmppath}/%{name}-buildroot

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
