Summary:	An enhanced front-end for the ghostscript PostScript(TM) interpreter
Name:		gv
Version:	3.7.4
Release:	1
License:	GPLv3
Group:		Publishing
Url:		http://www.gnu.org/software/gv/
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source11:	%{name}.png
Patch0:		gv-3.7.3-libXaw3d-1.6.patch
Patch1:		gv-3.6.3-gvuncompress.patch

BuildRequires:	imagemagick
BuildRequires:	texinfo
BuildRequires:	Xaw3d-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xt)

%rename		ghostview
Requires:	ghostscript-module-X

%description
Gv provides a user interface for the ghostscript PostScript(TM)
interpreter.  Derived from the ghostview program, gv can display
PostScript and PDF documents using the X Window System.

Install the gv package if you'd like to view PostScript and PDF documents
on your system.  You'll also need to have the ghostscript package
installed, as well as the X Window System.

%prep
%setup -q
%autopatch -p1

%build
# force regeneration of file
rm -f src/gv_intern_res_unix.dat

%configure \
	--with-scratch-dir=~/tmp/ \
	--enable-scrollbar-code
%make_build

%install
%make_install
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
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_infodir}/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

