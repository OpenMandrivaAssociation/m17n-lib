%define version	1.5.5
%define release	%mkrel 2

%define m17n_db_version   1.5.1
%define libotf_version    0.9.5

%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:      m17n-lib
Summary:   Multilingual text processing library
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   LGPLv2+
URL:       http://www.m17n.org/m17n-lib/index.html
Source0:   http://www.m17n.org/m17n-lib-download/%{name}-%{version}.tar.gz
Patch0:    m17n-lib-1.5.5-drop-versioninfo-from-module.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:        %{libname} = %{version}

# NOTE: medit and mdump require this font otherwise you get a SIGFPE
# because the font is not found, thus generating a tab_width=0 in
# layout_glyph_string() and then a division-by-zero.
# --> the bug is rather in the library and should be handled there.
Requires:        fonts-ttf-freefont

Requires:        m17n-db >= %{m17n_db_version}
Requires:        libotf >= %{libotf_version}
BuildRequires:   m17n-db-devel >= %{m17n_db_version}
BuildRequires:   automake
BuildRequires:   libxml2-devel, X11-devel
BuildRequires:   freetype2-static-devel
BuildRequires:   libgd-static-devel >= 2.0
BuildRequires:   libjpeg-static-devel
BuildRequires:   anthy-devel >= 6300d
BuildRequires:   libotf-devel >= %{libotf_version}
BuildRequires:   libfribidi-devel
# (tv) for AM_GNU_GETTEXT:
BuildRequires:   gettext-devel

%description
The m17n library is a multilingual text processing library for the C
language.


%package -n %{libname}
Summary:    The m17n library
Group:      System/Internationalization
Conflicts:  %{develname} < 1.5.5-2

%description -n %{libname}
m17n library.

%package -n %{develname}
Summary:    Headers of m17n for development
Group:      Development/C
Requires:   %{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}
Provides:   lib%{name}-devel = %{version}-%{release}
Obsoletes:  %{_lib}m17n-lib0-devel

%description -n %{develname}
Headers of %{name} for development.

%prep
%setup -q -n %name-%version
%patch0 -p0

%build
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# multiarch policy
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/m17n-config

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/m17n-conv
%{_bindir}/m17n-date
%{_bindir}/m17n-dump
%{_bindir}/m17n-edit
%{_bindir}/m17n-view

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libm17n*.so.%{major}*
%{_libdir}/libm17n-X.so
%{_libdir}/libm17n-gd.so
%{_libdir}/libmimx-anthy.so
%{_libdir}/libmimx-ispell.so

%files -n %{develname}
%defattr(-,root,root)
%{_bindir}/m17n-config
%multiarch %{multiarch_bindir}/m17n-config
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/libm17n.so
%{_libdir}/libm17n-core.so
%{_libdir}/libm17n-flt.so
%{_libdir}/libm17n-gui.so
%{_libdir}/pkgconfig/*
