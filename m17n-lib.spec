%define version	1.6.3
%define release	2

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
Requires:        %{libname} = %{version}

# NOTE: medit and mdump require this font otherwise you get a SIGFPE
# because the font is not found, thus generating a tab_width=0 in
# layout_glyph_string() and then a division-by-zero.
# --> the bug is rather in the library and should be handled there.
Requires:        fonts-ttf-freefont

Requires:        m17n-db >= %{m17n_db_version}
Requires:        libotf >= %{libotf_version}
BuildRequires:   m17n-db-devel >= %{m17n_db_version}
BuildRequires:   thai-devel
BuildRequires:   pkgconfig(libxml-2.0)
BuildRequires:	 fontconfig-devel
BuildRequires:	 pkgconfig(x11)
BuildRequires:	 pkgconfig(xaw7)
BuildRequires:	 pkgconfig(xft)
BuildRequires:	 pkgconfig(xt)
BuildRequires:	 gd-devel
BuildRequires:	 fribidi-devel
BuildRequires:   freetype-devel
BuildRequires:   anthy-devel >= 6300d
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
make

%install
%makeinstall_std

rm -f %buildroot%_libdir/m17n/*/*.la

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


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.2-2mdv2011.0
+ Revision: 661701
- multiarch fixes

* Mon Oct 04 2010 Funda Wang <fwang@mandriva.org> 1.6.2-1mdv2011.0
+ Revision: 582895
- fix build
- 1.6.2 final

* Thu Sep 23 2010 Funda Wang <fwang@mandriva.org> 1.6.2-0.RC.1mdv2011.0
+ Revision: 580660
- 1.6.2 RC

* Tue Apr 27 2010 Funda Wang <fwang@mandriva.org> 1.6.1-1mdv2011.0
+ Revision: 539485
- new version 1.6.1

* Tue Mar 30 2010 Funda Wang <fwang@mandriva.org> 1.6.0-1mdv2010.1
+ Revision: 529686
- fix BR on thai
- New version 1.6.0

* Sun Feb 14 2010 Funda Wang <fwang@mandriva.org> 1.5.5-2mdv2010.1
+ Revision: 505982
- finally fix m17n dlopen problem.

* Fri Aug 14 2009 Funda Wang <fwang@mandriva.org> 1.5.5-1mdv2010.0
+ Revision: 416295
- new version 1.5.5

* Sat Mar 07 2009 Funda Wang <fwang@mandriva.org> 1.5.4-1mdv2009.1
+ Revision: 351373
- New version 1.5.4

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5.3-2mdv2009.1
+ Revision: 301398
- rebuilt against new libxcb

* Tue Oct 21 2008 Funda Wang <fwang@mandriva.org> 1.5.3-1mdv2009.1
+ Revision: 295990
- New version 1.5.3

* Wed Sep 24 2008 Funda Wang <fwang@mandriva.org> 1.5.2-2mdv2009.0
+ Revision: 287761
- recognize new fribidi

* Thu Jun 26 2008 Funda Wang <fwang@mandriva.org> 1.5.2-1mdv2009.0
+ Revision: 229210
- fix requires
- New version 1.5.2

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Feb 07 2008 Funda Wang <fwang@mandriva.org> 1.5.1-1mdv2008.1
+ Revision: 163516
- disable parallel build
- New version 1.5.1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 28 2007 Funda Wang <fwang@mandriva.org> 1.4.0-1mdv2008.1
+ Revision: 138762
- New version 1.5.0

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jul 21 2007 Funda Wang <fwang@mandriva.org> 1.4.0-1mdv2008.0
+ Revision: 54233
- Use self-contained bootstrap
- New version


* Wed Jan 10 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.3.4-1mdv2007.0
+ Revision: 106863
- add buildrequires on gettext-devel for `AM_GNU_GETTEXT
- new release
- latest snapshot (UTUMI Hirosi <utuhiro78@yahoo.co.jp>)
- Import m17n-lib

* Wed Aug 16 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.3.3-3.20060803.2
- rebuild for fixed libxaw soname

* Fri Aug 04 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.3.3-3.20060803.1mdv2007.0
- latest snapshot
- (better Thai support)
- (http://sourceforge.net/mailarchive/forum.php?thread_id=26116958&forum_id=43684)
- update patch0 for latest m17n-lib

* Mon Jun 26 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.3.3-2.20060625.1mdv2007.0
- latest snapshot

* Sat Feb 25 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.3.3-1mdk
- new release
- move lib*.so to devel

* Thu Jan 19 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.3.1-1mdk
- new release

* Fri Dec 23 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.3.0-1mdk
- new release

* Wed Nov 16 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.2.0-7.20051116.1mdk
- latest snapshot
- update patch0

* Wed Aug 10 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.2.0-6.20050809.1mdk
- latest snapshot
- remove patch1 (merged upstream)

* Tue May 10 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.2.0-5.20050425.1mdk
- latest snapshot (UTUMI Hirosi <utuhiro78@yahoo.co.jp>)
- patch 1: fix compilation with gcc-4.0.0 (Kenichi Handa)

* Fri Mar 18 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.2.0-4mdk
- add "-a" to automake-1.8
- add symlink to ltmain.sh
- add autoheader-2.5x
- spec cleanup
- remove find_lang (it doesn't have po files)
- add some symlinks to libdir since SCIM/UIM open them (#14709)

* Wed Feb 16 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.2.0-3mdk
- multiarch and move m17n-config to -devel package
- hmmm, forgot a change from older tree, aka nuke explicit libfribidi0 dep

* Tue Feb 15 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.2.0-2mdk
- nuke lib64 rpaths (again)
- fix parallel build (again)

* Tue Dec 28 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.2.0-1mdk
- new release

* Fri Nov 26 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.1.0-4.cvs20041126.2mdk
- latest snapshot
- add BuildRequires: libotf-devel (for OpenType font support)
- add BuildRequires: libfribidi-devel (for Arabic/Hebrew support)

* Fri Oct 22 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.1.0-3mdk
- fix parallel build
- requires: fonts-ttf-freefont for medit, mdump

* Thu Aug 19 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.1.0-2mdk
- add BuildRequires:	libanthy-devel

* Wed Aug 18 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.0-1mdk
- new release
- only run bootstrap if needed

* Thu Jul 29 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.2-7.cvs20040714.3mdk
- remove requires on devel packages

* Sat Jul 24 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.0.2-7.cvs20040714.2mdk
- add BuildRequires: libjpeg-static-devel

* Wed Jul 21 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.2-7.cvs20040714.1mdk
- fix buildrequires
- cvs 20040714 (UTUMI Hirosi <utuhiro78@yahoo.co.jp>)

* Fri Jul 16 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.0.2-7.cvs20040619.2mdk
- add BuildRequires: freetype2-static-devel

* Sun Jun 20 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.0.2-7.cvs20040619.1mdk
- cvs 20040619
- remove patch0 (merged)

* Wed Jun 16 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.2-6mdk
- catch another buildrequires

* Tue Jun 15 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.0.2-5mdk
- add patch0 (made by James Su <suzhe@tsinghua.org.cn>) for scim-m17n

* Wed Jun 09 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.2-4mdk
- really fix buildrequires (I suck, I suck, I suck, I suck, I suck, I suck, I suck)

* Wed Jun 09 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.2-3mdk
- move plugins' *.so into main lib package since uim opens them through
  dlopen()

* Wed Jun 09 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.2-2mdk
- fix buildrequires
- proper use of %%mklibname

* Fri May 28 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.2-1mdk
- initial release (based on UTUMI Hirosi <utuhiro78@yahoo.co.jp> 's work)

