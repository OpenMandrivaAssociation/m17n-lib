%define major 0
%define libname %mklibname %{name} %{major}
%define libcore %mklibname %{name}-core %{major}
%define libflt %mklibname %{name}-flt %{major}
%define libgui %mklibname %{name}-gui %{major}
%define devname %mklibname -d %{name}

Summary:	Multilingual text processing library
Name:		m17n-lib
Version:	1.8.5
Release:	1
Group:		System/Internationalization
License:	LGPLv2+
Url:		https://www.m17n.org/m17n-lib/index.html
Source0:	http://savannah.c3sl.ufpr.br//m17n/m17n-lib-%{version}.tar.gz

BuildRequires:	gd-devel
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(anthy) >= 6300d
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(libotf)
BuildRequires:	pkgconfig(libthai)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(m17n-db)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xt)
# NOTE:	medit and mdump require this font otherwise you get a SIGFPE
# because the font is not found, thus generating a tab_width=0 in
# layout_glyph_string() and then a division-by-zero.
# --> the bug is rather in the library and should be handled there.
Requires:	fonts-ttf-freefont
Requires:	libotf
Requires:	m17n-db

%description
The m17n library is a multilingual text processing library for the C
language.

%package -n %{libname}
Summary:	The m17n library
Group:		System/Internationalization

%description -n %{libname}
m17n library.

%package -n %{libcore}
Summary:	The m17n library
Group:		System/Internationalization
Conflicts:	%{_lib}m17n-lib0 < 1.6.4-2

%description -n %{libcore}
m17n-core library.

%package -n %{libflt}
Summary:	The m17n library
Group:		System/Internationalization
Conflicts:	%{_lib}m17n-lib0 < 1.6.4-2

%description -n %{libflt}
m17n-flt library.

%package -n %{libgui}
Summary:	The m17n library
Group:		System/Internationalization
Conflicts:	%{_lib}m17n-lib0 < 1.6.4-2

%description -n %{libgui}
m17n-gui library.

%package -n %{devname}
Summary:	Headers of m17n for development
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libcore} = %{version}-%{release}
Requires:	%{libflt} = %{version}-%{release}
Requires:	%{libgui} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Headers of %{name} for development.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build -j1

%install
%make_install

%files
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/m17n-conv
%{_bindir}/m17n-date
%{_bindir}/m17n-dump
%{_bindir}/m17n-edit
%{_bindir}/m17n-view
%{_libdir}/m17n/*/*.so

%files -n %{libname}
%{_libdir}/libm17n.so.%{major}*

%files -n %{libcore}
%{_libdir}/libm17n-core.so.%{major}*

%files -n %{libflt}
%{_libdir}/libm17n-flt.so.%{major}*

%files -n %{libgui}
%{_libdir}/libm17n-gui.so.%{major}*

%files -n %{devname}
#%{_bindir}/m17n-config
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
