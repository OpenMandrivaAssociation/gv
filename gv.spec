Name:		gv
Version:	3.7.1
Release:	%mkrel 4
Summary:	An enhanced front-end for the ghostscript PostScript(TM) interpreter
License:	GPL
Group:		Publishing
URL:		http://www.gnu.org/software/gv/
# old source: ftp://thep.physik.uni-mainz.de/pub/gv/unix/%{name}-%{version}.tar.bz2
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source11:	%{name}.png
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
rm -rf %{buildroot}
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

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 200900
%{update_menus}
%endif
%_install_info gv.info

%preun
%_remove_install_info gv.info

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

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
