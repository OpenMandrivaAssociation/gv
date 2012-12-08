Name:		gv
Version:	3.7.1
Release:	6
Summary:	An enhanced front-end for the ghostscript PostScript(TM) interpreter
License:	GPL
Group:		Publishing
URL:		http://www.gnu.org/software/gv/
# old source: ftp://thep.physik.uni-mainz.de/pub/gv/unix/%{name}-%{version}.tar.bz2
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source11:	%{name}.png
BuildRequires:	imagemagick
BuildRequires:	libx11-devel
BuildRequires:	Xaw3d-devel
BuildRequires:	libxinerama-devel
BuildRequires:	libxmu-devel
BuildRequires:	libxt-devel
BuildRequires:	texinfo
Obsoletes:	ghostview
Provides:	ghostview
Requires:	ghostscript-module-X
Patch0:		gv-3.7.1-translation.patch
Patch1:		gv-3.6.3-gvuncompress.patch

%description
Gv provides a user interface for the ghostscript PostScript(TM)
interpreter.  Derived from the ghostview program, gv can display
PostScript and PDF documents using the X Window System.

Install the gv package if you'd like to view PostScript and PDF documents
on your system.  You'll also need to have the ghostscript package
installed, as well as the X Window System.

%prep
%setup -q
%patch0 -p1 -b .gvuncompress
%patch1 -p1 -b .gvuncompress

%build
# force regeneration of file
rm -f src/gv_intern_res_unix.dat

%configure2_5x \
	--with-scratch-dir=~/tmp/ \
	--enable-scrollbar-code
%make

%install
%makeinstall_std
install -m 0755 gvuncompress %{buildroot}%{_bindir}/gvuncompress

# icons
mkdir -p %{buildroot}%{_iconsdir} %{buildroot}%{_miconsdir}
install -m644 %{SOURCE11} -D %{buildroot}%{_liconsdir}/gv.png
convert -geometry 32x32 %{SOURCE11} %{buildroot}%{_iconsdir}/gv.png
convert -geometry 16x16 %{SOURCE11} %{buildroot}%{_miconsdir}/gv.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=gv
Comment=Viewer for Postscript and PDF files
Exec=%{_bindir}/gv %f
Icon=gv
Terminal=false
Type=Application
Categories=Office;Viewer;
EOF


%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_infodir}/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3.7.1-4mdv2011.0
+ Revision: 664963
- mass rebuild

* Thu Mar 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.7.1-3
+ Revision: 643722
- Avoid printing a Xt toolkit warning at startup

* Tue Dec 21 2010 Funda Wang <fwang@mandriva.org> 3.7.1-2mdv2011.0
+ Revision: 623675
- simplify BR

* Mon Aug 23 2010 Oden Eriksson <oeriksson@mandriva.com> 3.7.1-1mdv2011.0
+ Revision: 572388
- 3.7.1

* Sun Dec 27 2009 Frederik Himpe <fhimpe@mandriva.org> 3.6.8-1mdv2010.1
+ Revision: 482696
- update to new version 3.6.8

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.6.7-2mdv2010.0
+ Revision: 425084
- rebuild

* Sun Mar 22 2009 Frederik Himpe <fhimpe@mandriva.org> 3.6.7-1mdv2009.1
+ Revision: 360403
- update to new version 3.6.7

* Sun Jan 04 2009 JÃ©rÃ´me Soyer <saispo@mandriva.org> 3.6.6-1mdv2009.1
+ Revision: 324848
- New upstream release

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 3.6.3-4mdv2009.0
+ Revision: 218421
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 3.6.3-4mdv2008.1
+ Revision: 178956
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Aug 19 2007 Funda Wang <fwang@mandriva.org> 3.6.3-2mdv2008.0
+ Revision: 66742
- BR xaw3d
- BR texinfo to generate info file

* Sun Aug 19 2007 Funda Wang <fwang@mandriva.org> 3.6.3-1mdv2008.0
+ Revision: 66588
- New version 3.6.3
- rediff patch6
- CVE patch not needed anymore


* Sat Mar 10 2007 David Walluck <walluck@mandriva.org> 3.6.2-1mdv2007.1
+ Revision: 140427
- 3.6.2
  bunzip2 patches
  remove gv-3.6.1-scrollbar.patch (fixed upstream)
  remove automake requirement (needed by removed gv-3.6.1-scrollbar.patch)

* Thu Dec 07 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 3.6.1-10mdv2007.1
+ Revision: 91967
- Bumped release.
- Added security patch for CVE-2006-5864. Closes: #27209
- Moved autoreconf to build section.
- Removed some old stuff commented.

* Tue Nov 21 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 3.6.1-9mdv2007.1
+ Revision: 85793
- rebuilt

* Fri Nov 17 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 3.6.1-8mdv2007.1
+ Revision: 85155
- Bumped release.

* Fri Nov 17 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 3.6.1-7mdv2007.1
+ Revision: 85150
- Added missing BuildRequires to desktop-file-utils.
- Unversioned buildrequires.
- Filtered BuildRequires.
- Better version of scrollbar patch: do not alter ./configure directly
- Use of buildroot macro.
- Import gv

* Thu Sep 07 2006 Giuseppe Ghibò <ghibo@mandriva.com> 3.6.1-7mdv2007.0
- added dAlignToPixels=0 to workaround a ghostscript font aliasing problem
  (http://bugs.ghostscript.com/show_bug.cgi?id=687376), Patch8.
- xdg menus.

* Fri Feb 10 2006 Thierry Vignaud <tvignaud@mandriva.com> 3.6.1-6mdk
- fix build on x86_64

* Fri Jan 20 2006 Till Kamppeter <till@mandriva.com> 3.6.1-5mdk
- Really fixed bug 20200.

* Fri Jan 20 2006 Till Kamppeter <till@mandriva.com> 3.6.1-4mdk
- Fixed misbehaviour of the vertical scrollbar (patch 7, bug 20200,
  thanks to Juergen Holm, holm at theorie dot physik dot uni-goettingen 
  dot de).
- Rebuilt for X.org.
- Introduced %%mkrel.

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 3.6.1-3mdk
- Rebuild

* Sat Jan 15 2005 Abel Cheung <deaddog@mandrake.org> 3.6.1-2mdk
- rebuild

* Mon Dec 27 2004 Abel Cheung <deaddog@mandrake.org> 3.6.1-1mdk
- gv is now a GNU project
- New version
- Drop P1,3,7 (upstream), P2 (outdated), Rediff P6 (open compressed files)
- Integrate P5 later, I'm lazy
- Redo installation procedure since it uses autotools now
- Replace ugly icon with the one in GNOME high contrast theme, that's
  much better

* Sat Dec 25 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 3.5.8-33mdk
- fix buildrequires
- do parallell build
- fix summary-ended-with-dot

* Fri Jun 04 2004 Laurent Montel <lmontel@mandrakesoft.com> 3.5.8-32mdk
- Rebuild

