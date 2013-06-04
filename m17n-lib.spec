%define m17n_db_version   1.5.1
%define libotf_version    0.9.5

%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:      m17n-lib
Summary:   Multilingual text processing library
Version:   1.6.4
Release:   1
Group:     System/Internationalization
License:   LGPLv2+
URL:       http://www.m17n.org/m17n-lib/index.html
Source0:   http://savannah.c3sl.ufpr.br//m17n/m17n-lib-%version.tar.gz
Requires:        %{libname} = %{version}

# NOTE: medit and mdump require this font otherwise you get a SIGFPE
# because the font is not found, thus generating a tab_width=0 in
# layout_glyph_string() and then a division-by-zero.
# --> the bug is rather in the library and should be handled there.
Requires:        fonts-ttf-freefont

Requires:        m17n-db >= %{m17n_db_version}
Requires:        libotf >= %{libotf_version}
BuildRequires:   pkgconfig(m17n-db)
BuildRequires:   pkgconfig(libthai)
BuildRequires:   pkgconfig(libxml-2.0)
BuildRequires:	 pkgconfig(fontconfig)
BuildRequires:	 pkgconfig(x11)
BuildRequires:	 pkgconfig(xaw7)
BuildRequires:	 pkgconfig(xft)
BuildRequires:	 pkgconfig(xt)
BuildRequires:	 gd-devel
BuildRequires:	 pkgconfig(fribidi)
BuildRequires:   pkgconfig(freetype2)
BuildRequires:   pkgconfig(anthy) >= 6300d
BuildRequires:   pkgconfig(libotf) >= %{libotf_version}
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
%setup -q -n %{name}-%{version}

%build
%configure2_5x --disable-static
# -j8 broken as of 1.6.4
make

%install
%makeinstall_std

# multiarch policy
%multiarch_binaries %{buildroot}%{_bindir}/m17n-config

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/m17n-conv
%{_bindir}/m17n-date
%{_bindir}/m17n-dump
%{_bindir}/m17n-edit
%{_bindir}/m17n-view
%{_libdir}/m17n/*/*.so

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libm17n*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_bindir}/m17n-config
%{multiarch_bindir}/m17n-config
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
