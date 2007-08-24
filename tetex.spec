%define name            tetex
%define pkgname         tetex
%define version         3.0
%define docversion	3.0
%define pkgversion      3.0
%define tetexversion	3.0
%define tetexrelease    32
%define relsuffix	mdk
%if %{mdkversion} >= 200610
%define relsuffix	mdv2007.0
%endif
%if %{mdkversion} >= 200710
%define relsuffix	mdv2007.1
%endif
%if %{mdkversion} >= 200800
%define relsuffix	mdv2008.0
%endif
%define texmfversion    3.0
%define texmfsrcversion	3.0
%define texmfggversion	3.0k
%define texmfsrcggversion	3.0k
%define jadename	jadetex
%define jadeversion	3.12
%define jaderelease_delta 98
%define jaderelease	%(R=%{tetexrelease}; echo $((${R/%relsuffix/} + %{jaderelease_delta}))%relsuffix)
%define xmltexname	xmltex
%define xmltexversion	1.9
# reset the delta if changing the xmltexversion.
%define xmltexrelease_delta 46
%define xmltexrelease	%(R=%{tetexrelease}; echo $((${R/%relsuffix/} + %{xmltexrelease_delta}))%relsuffix)
%define csidxversion	19990820

%define vartexfonts	/var/lib/texmf
%define texmfsysvar	%{_datadir}/texmf-var
%define	texmfconfig	%{_datadir}/texmf-config

# 1 = have ghostscript >= 6.01 (e.g. Mandrake Linux >= 8.1)
# 0 = don't have ghostscript >= 6.01 (e.g. Mandrake Linux 8.0, 7.2, etc.)
%define haveghost6	1

Summary:	The TeX text formatting system
Name:		%{name}
Version:	%{version}
Release:	%{tetexrelease}%{relsuffix}
License:	Distributable
Group:		Publishing
#
Source0:	ftp://cam.ctan.org/tex-archive/systems/unix/teTeX/2.0/distrib/sources/%{name}-src-%{tetexversion}.tar.bz2
Source1:	ftp://cam.ctan.org/tex-archive/systems/unix/teTeX/2.0/distrib/sources/%{name}-texmf-%{texmfversion}.tar.bz2
Source3:	ftp://cam.ctan.org/tex-archive/systems/unix/teTeX/2.0/distrib/sources/%{name}-texmfsrc-%{texmfsrcversion}.tar.bz2
Source4:	icons-xdvi.tar.bz2
Source5:	http://peoples.mandrakesoft.com/~ghibo/%{name}-texmf-extras-gg-%{texmfggversion}.tar.bz2
Source6:	http://peoples.mandrakesoft.com/~ghibo/%{name}-texmfsrc-extras-gg-%{texmfsrcggversion}.tar.bz2
Source7:	http://prdownloads.sourceforge.net/jadetex/%{jadename}-%{jadeversion}.tar.bz2
Source8:	ftp://ftp.dante.de/pub/tex/macros/xmltex.tar.bz2
Source10:	tetex.cron
Source11:	ftp://math.feld.cvut.cz/pub/cstex/tetex-rpm/mandrake/csindex-%{csidxversion}.tar.bz2
Source20:	ttf2pk.tar.bz2
Source21:	dvipdfpress.bz2
#
Patch0:		%{name}-3.0-texmfcnf.patch
Patch1:		%{name}-3.0-fmtutil.patch
Patch3:		%{name}-3.0-mf-mainmemory.patch
Patch4:		%{name}-3.0-mp-mainmemory.patch
Patch5:		%{name}-3.0-xdvik-dot.patch
Patch6:		%{name}-3.0-epstopdf-dct.patch
Patch10:	%{name}-3.0-ttf2pk.patch
Patch11:	%{name}-3.0-badscript.patch
Patch12:	%{name}-3.0-dvipdfm-security.patch
Patch14:	%{name}-3.0-mfw.patch
Patch15:	%{name}-3.0-CAN-2004-0888.patch
Patch16:	%{name}-3.0-CAN-2005-0064.patch
Patch17:	%{name}-3.0-xpdf-CAN-2005-0206.patch
Patch18:	tetex-src-3.0-pic.patch
Patch20:	%{name}-1.0-texmf-dvipsgeneric.patch
Patch21:	%{name}-3.0-xdvi-www.patch
Patch23:	%{name}-%{jadename}-%{jadeversion}-basque.patch
Patch24:	%{name}-%{jadename}-%{jadeversion}-theta.patch
Patch25:	passivetex-1.23.patch
Patch26:	passivetex-1.24.patch
Patch27:	passivetex-1.25.patch
Patch28:	%{name}-3.0-texdoc-wwwbrowser.patch
Patch29:	tetex-3.0-ttf2pk-use-local-libtool.patch
Patch30:	tetex-src-3.0-cvs20050823a.patch
Patch31:	tetex-src-3.0-t1lib-autoconf.patch
Patch32:	koffce-xpdf-CVE-2007-0104.patch
Patch33:	tetex-3.0-kpathsea-numargs.patch
Patch34:	tetex-3.0-manfix.patch
Patch35:	tetex-3.0-simpdftex.patch
Patch36:	tetex-3.0-pdftex1401.patch
Patch37:	tetex-3.0-pdftex1401-remove.patch
Patch38:	tetex-3.0-xdvizilla.patch
Patch39:	tetex-3.0-pdftex1403.patch
Patch40:	tetex-3.0-pdftosrc.patch
Patch41:	tetex-3.0-kpathsea-cnf.patch
Patch42:	tetex-3.0-cweb.patch
Patch43:	tetex-3.0-makeindex-CVE-2007-0650.patch
Patch44:	tetex-3.0-mktexlsr.patch
#
URL:		http://www.tug.org/teTeX/
Packager:	Giuseppe Ghibò <ghibo@mandriva.com>
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	tmpwatch
Requires:	dialog
Requires:	ed
Requires:	info-install
Requires:	sam2p
BuildRequires:	autoconf2.1
BuildRequires:	automake1.7
BuildRequires:	bison
BuildRequires:	ed
BuildRequires:	flex
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	lesstif-devel
BuildRequires:	ncurses-devel
BuildRequires:	png-devel
BuildRequires:	xpm-devel
BuildRequires:	XFree86-devel
%if %{mdkversion} >= 200610
BuildRequires:  desktop-file-utils
%endif
Obsoletes:	cweb
Provides:	cweb
Conflicts:      texlive-texmf

%description
teTeX is an implementation of TeX for Linux or UNIX systems. TeX takes
a text file and a set of formatting commands as input and creates a
typesetter independent .dvi (DeVice Independent) file as output.
Usually, TeX is used in conjunction with a higher level formatting
package like LaTeX or PlainTeX, since TeX by itself is not very
user-friendly.

Install teTeX if you want to use the TeX text formatting system.  If
you are installing teTeX, you will also need to install tetex-afm (a
PostScript(TM) font converter for TeX), tetex-dvilj (for converting
.dvi files to HP PCL format for printing on HP and HP compatible
printers), tetex-dvips (for converting .dvi files to PostScript format
for printing on PostScript printers), tetex-latex (a higher level
formatting package which provides an easier-to-use interface for TeX)
and tetex-xdvi (for previewing .dvi files in X).  Unless you're an
expert at using TeX, you'll also want to install the tetex-doc
package, which includes the documentation for TeX.

%package	latex
Summary:	The LaTeX front end for the TeX text formatting system
Group:		Publishing
Requires:	tetex = %{PACKAGE_VERSION}
%if %{mdkversion} < 200610
Requires:	tetex-dvips
%else
Requires:	ghostscript-dvipdf
%endif
Provides:	prosper
Obsoletes:	prosper
Provides:	latex-xcolor
Obsoletes:	latex-xcolor
Provides:	latex-pgf
Obsoletes:	latex-pgf

%description	latex
LaTeX is a front end for the TeX text formatting system.  Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

If you are installing teTeX, so that you can use the TeX text formatting
system, you will also need to install tetex-latex.  In addition, you will
need to install tetex-afm (for converting PostScript font description
files), tetex-dvilj (for converting .dvi files to HP PCL format for
printing on HP and HP compatible printers), tetex-dvips (for converting
.dvi files to PostScript format for printing on PostScript printers) and
tetex-xdvi (for previewing .dvi files in X).  If you're not an expert
at TeX, you'll probably also want to install the tetex-doc package,
which contains documentation for TeX.

%package	xdvi
Summary:	An X viewer for DVI files
Group:		Publishing
Requires:	tetex = %{PACKAGE_VERSION}
%if %{mdkversion} >= 200610
Requires:	xmessage
%else
Requires:	X11R6-contrib
%endif

%description	xdvi
Xdvi allows you to preview the TeX text formatting system's output .dvi
files on an X Window System.

If you are installing teTeX, so that you can use the TeX text formatting    
system, you will also need to install tetex-xdvi.  In addition, you will
need to install tetex-afm (a PostScript font converter for TeX),
tetex-dvilj (for converting .dvi files to HP PCL format for printing on
HP and HP compatible printers), tetex-dvips (for converting .dvi files to
PostScript format for printing on PostScript printers), and tetex-latex
(a higher level formatting package which provides an easier-to-use
interface for TeX).  If you're not a TeX expert, you'll probably also
want to install the tetex-doc package, which contains documentation for
the TeX text formatting system.

%package	dvips
Summary:	A DVI to PostScript converter for the TeX text formatting system
Group:		Publishing
Requires:	tetex = %{PACKAGE_VERSION}

%description	dvips
Dvips converts .dvi files produced by the TeX text formatting system
(or by another processor like GFtoDVI) to PostScript(TM) format.
Normally the PostScript file is sent directly to your printer.

If you are installing teTeX, so that you can use the TeX text formatting
system, you will also need to install tetex-dvips.  In addition, you will
need to install tetex-afm (for converting PostScript font description
files), tetex-dvilj (for converting .dvi files to HP PCL format for
printing on HP and HP compatible printers), tetex-latex (a higher level
formatting package which provides an easier-to-use interface for TeX) and
tetex-xdvi (for previewing .dvi files in X).  If you're installing TeX
and you're not an expert at it, you'll also want to install the tetex-doc
package, which contains documentation for the TeX system.

%package	dvilj
Summary:	A DVI to HP PCL (Printer Control Language) converter
Group:		Publishing
Requires:	tetex = %{PACKAGE_VERSION}

%description	dvilj
Dvilj and dvilj's siblings (included in this package) will convert TeX
text formatting system output .dvi files to HP PCL (HP Printer Control
Language) commands.  Using dvilj, you can print TeX files to HP
LaserJet+ and fully compatible printers.  With dvilj2p, you can print
to HP LaserJet IIP and fully compatible printers. And with dvilj4, you
can print to HP LaserJet4 and fully compatible printers.

If you are installing teTeX, so that you can use the TeX text formatting
system, you will also need to install tetex-dvilj.  In addition, you will
need to install tetex-afm (for converting PostScript font description
files), tetex-dvips (for converting .dvi files to PostScript format for
printing on PostScript printers), tetex-latex (a higher level formatting
package which provides an easier-to-use interface for TeX) and tetex-xdvi
(for previewing .dvi files in X).  If you're installing TeX and you're
not a TeX expert, you'll also want to install the tetex-doc package,
which contains documentation for TeX.

%package	afm
Summary:	A converter for PostScript(TM) font metric files, for use with TeX
Group:		Publishing
Requires:	tetex = %{PACKAGE_VERSION}

%description	afm
tetex-afm provides afm2tfm, a converter for PostScript font metric files. 
PostScript fonts are accompanied by .afm font metric files which describe
the characteristics of each font.  To use PostScript fonts with TeX, TeX
needs .tfm files that contain similar information.  Afm2tfm will convert
.afm files to .tfm files.  

If you are installing tetex in order to use the TeX text formatting system,
you will need to install tetex-afm.  You will also need to install
tetex-dvilj (for converting .dvi files to HP PCL format for printing on HP
and HP compatible printers), tetex-dvips (for converting .dvi files to
PostScript format for printing on PostScript printers), tetex-latex (a
higher level formatting package which provides an easier-to-use interface
for TeX) and tetex-xdvi (for previewing .dvi files in X).  Unless you're
an expert at using TeX, you'll probably also want to install the tetex-doc
package, which includes documentation for TeX.

%package	doc
Summary:	The documentation files for the TeX text formatting system
Group:		Books/Other
Requires:	tetex-xdvi
%define _requires_exceptions pear

%description	doc
The tetex-doc package contains documentation for the TeX text
formatting system.

If you want to use TeX and you're not an expert at it, you should
install the tetex-doc package.  You'll also need to install the tetex
package, tetex-afm (a PostScript font converter for TeX), tetex-dvilj
(for converting .dvi files to HP PCL format for printing on HP and HP
compatible printers), tetex-dvips (for converting .dvi files to
PostScript format for printing on PostScript printers), tetex-latex
(a higher level formatting package which provides an easier-to-use
interface for TeX) and tetex-xdvi (for previewing .dvi files).

%package	dvipdfm
Summary:	A DVI to PDF converter
Group:		Publishing
Requires:	tetex = %{PACKAGE_VERSION}
Requires:	tetex-dvips = %{PACKAGE_VERSION}
Requires:	ghostscript
%if %{mdkversion} >= 200610
Requires:	ghostscript-dvipdf
%endif

%description	dvipdfm
dvidpfm is a DVI to PDF translator for use with TeX.

%package	mfwin
Summary:	Metafont with output window
Group:		Publishing
Requires:	tetex = %{PACKAGE_VERSION}

%description	mfwin
This package contains METAFONT with window support. Install this
package if you plan to run METAFONT interactively and would like to see
the font building in a output window.

%package	devel
Summary:	Development libraries (kpathsea) for teTeX
Group:		Development/C
Requires:	tetex = %{PACKAGE_VERSION}

%description	devel
This package contains C headers and libraries, for developing TeX
applications using kpathsea library.

%package -n	%{jadename}
Summary:	TeX macros used by Jade TeX output.
Version: 	%{jadeversion}
Release:	%{jaderelease}
Group:		Publishing
License: 	Distributable (C) Sebastian Rahtz <s.rahtz@elsevier.co.uk>
URL: 		http://sourceforge.net/projects/jadetex
Requires: 	sgml-common >=  0.6.3-2mdk
Requires: 	tetex >= 1.0.7-51mdk
Requires: 	tetex-latex >= 1.0.7-51mdk
Requires: 	tetex-dvips >= 1.0.7-51mdk
Requires: 	openjade >= 1.3.1

%description -n	%{jadename}
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as TeX files, to obtain DVI, Postscript
or PDF files for example.

%package -n	%{xmltexname}
Summary:	Namespace-aware XML parser written in TeX.
Version: 	%{xmltexversion}
Release:	%{xmltexrelease}
Group:		Publishing
License: 	LaTeX Project Public License
URL: 		http://www.dcarlisle.demon.co.uk/xmltex/manual.html
Requires: 	tetex >= 1.0.7-52mdk
Requires: 	tetex-latex >= 1.0.7-52mdk

%description -n	%{xmltexname}
Namespace-aware XML parser written in TeX. This package
also includes passivetex macros, which can be used to process an XML
document which results from an XSL trasformation to formatting objects.

%package	context
Summary:	Document engineering system based on TeX
Group:		Publishing
Requires:	tetex >= 2.0.2

%description	context
CONTeXT is a document engineering system based on TeX. TeX is a
typesetting system and a program to typeset and produce documents.
CONTeXT is easy to use and enables you to make complex paper and
electronic documents.

%package	texi2html
Summary:	Convert texinfo (GNU docs) directly to HTML for easy reading
Group:		Publishing
License:	GPL
Provides:	texi2html
Obsoletes:	texi2html

%description	texi2html
This package converts the GNU standard form of documentation (texinfo) into
HTML files which can be read with any WWW browser.

%package	usrlocal
Summary:	Virtual package for placing local system-wide teTeX files
Group:		Publishing
License:	GPL

%description	usrlocal
This packages provides just the directory /usr/local/share/texmf
which is defined by the var TEXMFLOCAL in the default config file
and can be used for system-wide teTeX files.

%prep
%setup -q -n %{name}-src-%{tetexversion} -a 7 -a 8 -a 11 -a 20
chmod 755 csindex-%{csidxversion}
%patch0 -p1 -b .texmfcnf
%patch1 -p1 -b .fmtutil
%patch3 -p1 -b .mf-mainmem
%patch4 -p1 -b .mp-mainmem
%patch5 -p1 -b .xdvikdot
%patch6 -p1 -b .epstopdf
%patch10 -p1 -b .ttf2pk
%patch11 -p1 -b .badscript
%patch12 -p1 -b .dvipdfm
%patch14 -p1 -b .mfw
%patch15 -p1 -b .CAN-2004-0888
%patch16 -p1 -b .CAN-2005-0064
%patch17 -p1 -b .xpdf-CAN-2005-0206
%patch18 -p1 -b .pic

mkdir -p texmf
bzip2 -cd %{SOURCE1} | tar xf - -C texmf
bzip2 -cd %{SOURCE5} | tar xf - -C texmf
cp -p texmf/metafont/config/mf.ini texmf/metafont/config/mf-nowin.ini

# dvips config.generic
%patch20 -p1

# www-browser instead of netscape
%patch21 -p1 

# languages

# basque for jadetex
%patch23 -p1
%patch24 -p1

# passivetex 1.25
%patch25 -p1
%patch26 -p1
%patch27 -p1

%patch28 -p1 -b .wwwbrowser
%patch29 -p1 -b .local-libtool

# cvs 20050823
%patch30 -p1 -E
%patch31 -p1 -b .t1auto

# CVE-2007-0104
pushd libs
%patch32 -p3 -b .cve-2007-0104
popd

%patch33 -p1 -b .numargs
%patch34 -p1 -b .manfix
%patch35 -p1 -b .simpdf

# pdftex 1.40.1
%patch36 -p1
%patch37 -p1 -E
(cd texk/web2c && rm -rf pdfetexdir)

%patch38 -p1 -b .xdvizilla

# pdftex 1.40.3
%patch39 -p1 -b .pdf1403

%patch40 -p1 -b .pdftosrc
%patch41 -p1 -b .kpathsea

# cweb (cwebmac.tex)
%patch42 -p1

# CVE-2007-0650
%patch43 -p1 -b .cve-2007-0650

%patch44 -p1 -b .mktexlsr

# cleaning old latin modern 0.92.
(rm -f texmf/fonts/enc/dvips/lm/{cork-lm,qx-lm,qx-lmtt,texnansi-lm,ts1-lm}.enc
 rm -f texmf/fonts/map/dvips/lm/{cork-lm,lm,qx-lm,texnansi-lm,ts1-lm}.map
 rm -f texmf/fonts/tfm/public/lm/cork-*.tfm
)

# clean old pstricks
(cd texmf/doc/generic/pstricks
 rm -f exemplesUml.tex psgomanual.pdf pst-3dplot-doc.pdf pst-blur.pdf \
       pst-circ.pdf pst-gr3d.pdf pst-lens.pdf pst-math.pdf \
       pstricks-add-doc.pdf pst-slpe.pdf pst-uml-doc.pdf \
       README.* t2-ghsb.tex tst-poly.tex vue3d-e.pdf
)

# ttf2pk
(cd ttf2pk; rm -f configure; aclocal-1.7; autoconf)

find . -type f -print0 | xargs -0 chmod u+rw,go+r

## cputoolize to get updated config.{sub,guess}
#%{?__cputoolize: %{__cputoolize} -c libs/ncurses}
#%{?__cputoolize: %{__cputoolize} -c libs/libwww}
#%{?__cputoolize: %{__cputoolize} -c texk}
#%{?__cputoolize: %{__cputoolize} -c utils/texinfo}


%build
perl -pi -e 's@^vartexfonts\s*=\s.*@vartexfonts = %vartexfonts@g' texk/make/paths.mk
set -x
unset HOME || :
unset TEXINPUTS || :
#WANT_AUTOCONF_2_1=1 
sh ./reautoconf
%configure \
	--with-system-ncurses \
	--with-system-zlib \
	--with-system-pnglib \
	--disable-multiplatform \
	--without-dialog \
	--without-texinfo

make all

# jadetex
(CURRENTDIR=`pwd`
 cd %{jadename}-%{jadeversion}
 mkdir -p $CURRENTDIR/texmf/tex/jadetex
 install -m 644 dsssl.def dummyels.sty jadetex.cfg jadetex.ini \
	jadetex.ins jadetex.ltx mlnames.sty ucharacters.sty \
	pdfjadetex.ini uentities.sty unicode.sty ut1omlgc.fd \
	$CURRENTDIR/texmf/tex/jadetex
)

# xmltex
(CURRENTDIR=`pwd`
 mkdir -p $CURRENTDIR/texmf/tex/xmltex/{base,config,passivetex}
 mkdir -p $CURRENTDIR/texmf/doc/xmltex/{base,passivetex}
 (cd %{xmltexname}/base
  cp -p xmltex.tex *.xmt $CURRENTDIR/texmf/tex/xmltex/base
  cp -p *.ini xmltex.cfg $CURRENTDIR/texmf/tex/xmltex/config
  cp -p *.xml manual.tex test*.tex test*.cfg $CURRENTDIR/texmf/doc/xmltex/base
 )
 (cd %{xmltexname}/contrib/passivetex
  cp -p *.xmt *.sty $CURRENTDIR/texmf/tex/xmltex/passivetex
 )
)

# ttf2pk TrueType support (CJK extensions)
(cd ttf2pk
 mkdir -p extras/{include,lib}
 ln -sf ../../../texk/kpathsea extras/include/kpathsea
 ln -sf ../../../texk/kpathsea/.libs/libkpathsea.a extras/lib/libkpathsea.a
 rm -f config.cache config.log
 ./configure --with-kpathsea-dir=./extras
 make
)

# csindex
(cd csindex-%{csidxversion}
 make CC="gcc $RPM_OPT_FLAGS"
)


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/texmf \
	$RPM_BUILD_ROOT%{texmfsysvar} \
	$RPM_BUILD_ROOT%{vartexfonts} \
	$RPM_BUILD_ROOT/usr/local/share/texmf
	
tar cf - texmf | tar xf - -C $RPM_BUILD_ROOT%{_datadir}

export TEXMFLOCAL=$RPM_BUILD_ROOT/usr/local/share/texmf
export TEXMFSYSVAR=$RPM_BUILD_ROOT%{texmfsysvar}
export TEXMFSYSCONFIG=$RPM_BUILD_ROOT%{texmfconfig}
export VARTEXFONTS=$RPM_BUILD_ROOT%{vartexfonts}
export PATH=$RPM_BUILD_ROOT/%{_bindir}:$PATH
export TEXMF=$RPM_BUILD_ROOT%{_datadir}/texmf
%makeinstall texmf=$RPM_BUILD_ROOT%{_datadir}/texmf

# clean initial %{vartexfonts}
rm -rf $RPM_BUILD_ROOT%{vartexfonts}/*

# xdvi
install -m 755 texk/xdvik/t1mapper $RPM_BUILD_ROOT%{_bindir}
install -m 644 texk/xdvik/t1mapper.1 $RPM_BUILD_ROOT%{_mandir}/man1/

# csindex
(cd csindex-%{csidxversion}
 install -c -s -m 0755 csindex $RPM_BUILD_ROOT%{_bindir}
)

# jadetex man page
(cd %{jadename}-%{jadeversion}
 install -m 644 jadetex.1 pdfjadetex.1 $RPM_BUILD_ROOT%{_mandir}/man1
)

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
#bzip2 -9f $RPM_BUILD_ROOT%{_infodir}/*info* || true

# these are links

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily
install -m 755 %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily

#
# Add TrueType Support ttf2pk (CJK extensions)
cp -f ttf2pk/ttf2pk ttf2pk/ttf2tfm $RPM_BUILD_ROOT%{_bindir}
cp -f ttf2pk/ttf2pk.1 ttf2pk/ttf2tfm.1 $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/texmf/ttf2pk
cp -f ttf2pk/data/* $RPM_BUILD_ROOT%{_datadir}/texmf/ttf2pk

# Fix permission for directory "/usr/share/texmf/fonts/tfm/jknappen"
find $RPM_BUILD_ROOT%{_datadir}/texmf -type d -print | xargs chmod 755

# We keep the .log files for format .fmt files (useful to know how
# they are generated (included files, memory, etc.);
# strip buildroot path from .log files.
perl -pi -e "s@%{buildroot}@@g" $RPM_BUILD_ROOT%{texmfsysvar}/web2c/*.log

# call the spec-helper before creating the file list
# (thanks to Pixel).
s=/usr/share/spec-helper/spec-helper ; [ -x $s ] && $s

### Files list
rm -f filelist.*
find $RPM_BUILD_ROOT -type f -or -type l | \
	sed -e "s|$RPM_BUILD_ROOT||g" | \
	grep -v "^/etc" | grep -v ".orig$" | \
	sed -e "s|.*\.cnf$|%config(noreplace) &|" \
            -e "s|%{_datadir}/texmf/dvips/config/config\.ps$|%config(noreplace) &|" \
	    -e "s|%{_datadir}/texmf/dvips/config/config\.\(generic\|pdf\|www\)$|%config &|" \
	    -e "s|%{_datadir}/texmf/dvipdfm/config/config|%config(noreplace) &|" \
	    -e "s|%{_datadir}/texmf/xdvi/XDvi|%config &|" \
	    -e "s|%{_datadir}/texmf/tex/generic/config/.*|%config &|" \
	    -e "s|%{_datadir}/texmf/tex/dvips/config/updmap$|%config(noreplace) &|" \
	    -e "s|^%{_infodir}\(.*\)|%attr(644,root,root) \%{_infodir}\1.\*|" \
	    -e "s|^%{_mandir}\(.*\)|%attr(644,root,root) \%{_mandir}\1.\*|" > filelist.full

find $RPM_BUILD_ROOT%{_datadir}/texmf* \
	-type d | \
	sed "s|^$RPM_BUILD_ROOT|\%attr(-,root,root) \%dir |" >> filelist.full

# dir for TEXMFLOCAL
#echo "%attr(755,root,root) %dir /usr/local/share/texmf" >> filelist.full

# subpackages
grep -v "/doc/" filelist.full | grep latex | \
	grep -v "%{_datadir}/texmf/tex/latex/context" | \
	grep -v "%{_datadir}/context/data/latex-scite.properties" \
		> filelist.latex

grep -v "/doc/" filelist.full | grep jadetex	> filelist.jadetex

grep -v "/doc/" filelist.full | grep xmltex	> filelist.xmltex

grep -v "/doc/" filelist.full | grep xdvi | \
	grep -v "%{_datadir}/texmf/tex"		> filelist.xdvi

echo "%{_bindir}/mf" >> filelist.mfwin
echo "%{_bindir}/mfw" >> filelist.mfwin
echo "%{_datadir}/texmf/metafont/config/mf.ini" >> filelist.mfwin

echo "%{_bindir}/t1mapper" >> filelist.xdvi
echo "%attr(644,root,root) %{_mandir}/man1/t1mapper.1.*" >> filelist.xdvi

grep -v "/doc/" filelist.full | \
	grep "%{_includedir}" > filelist.devel
echo "%attr(-,root,root) %dir %{_includedir}/kpathsea" >> filelist.devel
echo "%{_libdir}/libkpathsea.la" >> filelist.devel
echo "%{_libdir}/libkpathsea.a" >> filelist.devel

grep -v "/doc/" filelist.full | grep dvips | \
	grep -v "%{_datadir}/%{texmfsysvar}/fonts/map/dvips/updmap" | \
	grep -v "%{_datadir}/texmf/tex" | \
	grep -v "%{_datadir}/texmf/dvips/config/config.ps" > filelist.dvips
echo "%{_bindir}/dvired" >> filelist.dvips
echo "%{_bindir}/dvi2fax" >> filelist.dvips

grep -v "/doc/" filelist.full | grep dvipdfm | \
	grep -v "%{_datadir}/texmf/tex"	|
	grep -v "%{_datadir}/texmf/dvipdfm/config/config" |
	grep -v "%{_datadir}/texmf/dvips" > filelist.dvipdfm
echo "%{_bindir}/ebb" >> filelist.dvipdfm
echo "%{_bindir}/dvipdft" >> filelist.dvipdfm

grep -v "/doc/" filelist.full | grep dvilj | \
	grep -v "%{_datadir}/texmf/tex/latex" 	> filelist.dvilj

grep -v "/doc/" filelist.full | grep afm 	> filelist.afm

grep "/doc/" filelist.full 			> filelist.doc
echo "%{_bindir}/texdoc" >> filelist.doc
echo "%{_bindir}/texdoctk" >> filelist.doc

grep -v "/doc/" filelist.full | grep -v fonts | \
	grep -v dvips | \
	grep -v pdftex/config | \
	grep context 	> filelist.context
cat >> filelist.context <<EOF
%{_bindir}/mptopdf
%{texmfsysvar}/web2c/cont-en.fmt
%{texmfsysvar}/web2c/cont-en.log
%{texmfsysvar}/web2c/metafun.log
%{texmfsysvar}/web2c/metafun.mem
%{texmfsysvar}/web2c/mptopdf.fmt
%{texmfsysvar}/web2c/mptopdf.log
EOF

cat > filelist.texi2html <<EOF
%{_bindir}/texi2html
%attr(644,root,root) %{_mandir}/man1/texi2html.1.*
%{_datadir}/texinfo/html/texi2html.html
%{_infodir}/texi2html.info.*
EOF

# now files listed only once, i.e. not included in any subpackage, will
# go in the main package
cat filelist.full \
    filelist.latex \
    filelist.xdvi \
    filelist.devel \
    filelist.dvips \
    filelist.dvilj \
    filelist.afm \
    filelist.doc \
    filelist.dvipdfm \
    filelist.mfwin \
    filelist.jadetex \
    filelist.xmltex \
    filelist.context \
    filelist.texi2html | \
    sort | uniq -u > filelist.main

# xdvi menu things
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/tetex-xdvi <<EOF
?package(tetex-xdvi): command="%{_bindir}/xdvi" needs="X11" \
icon="dvi.png" section="Applications/Publishing" title="XDvi" \
%if %{mdkversion} >= 200610
xdg=true \
%endif
longtitle="DVI files viewer"
EOF

%if %{mdkversion} >= 200610
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=XDVI
Comment=Viewer for TeX DVI files
Exec=%{_bindir}/xdvi %f
Icon=dvi
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Office-Publishing;Graphics;Office;Viewer;
Encoding=UTF-8
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-Office-Publishing" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*
%endif

# mdk icons
install -d $RPM_BUILD_ROOT%{_iconsdir}
tar xjvf %{SOURCE4} -C $RPM_BUILD_ROOT%{_iconsdir}

# %_docdir link.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc
ln -sf ../../..%{_datadir}/texmf/doc $RPM_BUILD_ROOT%{_datadir}/doc/tetex-doc-%{docversion}

# add dvipdfpress
bzip2 -cd %{SOURCE21} > $RPM_BUILD_ROOT%{_bindir}/dvipdfpress

# fix permissions for files generated with fmtutil-sys --all in make install
# stage
find $RPM_BUILD_ROOT -type f -print0 | xargs -0 chmod u+rw,go+r
find $RPM_BUILD_ROOT -type d -print0 | xargs -0 chmod u+rw,go+r

%clean
rm -rf $RPM_BUILD_ROOT
rm -f filelist.*

# make sure ls-R used by teTeX is updated after an install
%post
/sbin/install-info %{_infodir}/web2c.info.* %{_infodir}/dir
/sbin/install-info %{_infodir}/kpathsea.info.* %{_infodir}/dir
/usr/bin/env - /usr/bin/texhash 2> /dev/null
if [ -e %{texmfconfig}/web2c/updmap.cfg ]; then
	%{_bindir}/updmap-sys --quiet
fi
exit 0

%post latex
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
/sbin/install-info %{_infodir}/latex.info.* %{_infodir}/dir
exit 0

%post xdvi
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
%{update_menus}
exit 0

%post dvips
/sbin/install-info %{_infodir}/dvips.info.* %{_infodir}/dir
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%post dvilj
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%post afm
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0


%post dvipdfm
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%post mfwin
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%post -n %{jadename}
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%post -n %{xmltexname}
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%post context
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%post texi2html
/sbin/install-info %{_infodir}/texi2html.info.* %{_infodir}/dir

%post usrlocal
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun latex
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun xdvi
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
if [ "$1" = "0" ]; then
%{clean_menus}
fi
exit 0

%postun dvips
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun dvilj
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun afm
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun dvipdfm
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun mfwin
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun -n %{jadename}
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun -n %{xmltexname}
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun context
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun usrlocal
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --delete %{_infodir}/kpathsea.info.* %{_infodir}/dir
	/sbin/install-info --delete %{_infodir}/web2c.info.* %{_infodir}/dir
fi

%preun dvips
if [ "$1" = 0 ]; then
	/sbin/install-info --delete %{_infodir}/dvips.info.* %{_infodir}/dir
fi

%preun latex
if [ "$1" = 0 ]; then
	/sbin/install-info --delete %{_infodir}/latex.info.* %{_infodir}/dir
fi

%preun texi2html
if [ "$1" = 0 ]; then
	/sbin/install-info --delete %{_infodir}/texi2html.info.* %{_infodir}/dir
fi

%triggerpostun -- tetex < 3.0-31mdv2007.1
if [ "$2" -ge 1 ]; then
	if [ -e %{texmfconfig}/web2c/updmap.cfg ]; then
        	if [ -x %{_bindir}/updmap-sys ]; then
			grep -q "^Map cork-lm.map" %{texmfconfig}/web2c/updmap.cfg && %{_bindir}/updmap-sys --quiet --disable cork-lm.map
			grep -q "^Map qx-lm.map" %{texmfconfig}/web2c/updmap.cfg && %{_bindir}/updmap-sys --quiet --disable qx-lm.map
			grep -q "^Map texnansi-lm.map" %{texmfconfig}/web2c/updmap.cfg && %{_bindir}/updmap-sys --quiet --disable texnansi-lm.map
			grep -q "^Map ts1-lm.map" %{texmfconfig}/web2c/updmap.cfg && %{_bindir}/updmap-sys --quiet --disable ts1-lm.map

			grep -q "^Map lm-ec.map" %{texmfconfig}/web2c/updmap.cfg || %{_bindir}/updmap-sys --quiet --enable Map=lm-ec.map
			grep -q "^Map lm-qx.map" %{texmfconfig}/web2c/updmap.cfg || %{_bindir}/updmap-sys --quiet --enable Map=lm-qx.map
			grep -q "^Map lm-t5.map" %{texmfconfig}/web2c/updmap.cfg || %{_bindir}/updmap-sys --quiet --enable Map=lm-t5.map
			grep -q "^Map lm-texnansi.map" %{texmfconfig}/web2c/updmap.cfg || %{_bindir}/updmap-sys --quiet --enable Map=lm-texnansi.map
			grep -q "^Map lm-ts1.map" %{texmfconfig}/web2c/updmap.cfg || %{_bindir}/updmap-sys --quiet --enable Map=lm-ts1.map
		fi
	fi
fi
exit 0

%files -f filelist.main
%defattr(-,root,root)
%attr(1777,root,root) %dir %{vartexfonts}
%config %{_sysconfdir}/cron.daily/tetex.cron

%files -f filelist.latex latex
%defattr(-,root,root)

%files -f filelist.xdvi xdvi
%defattr(-,root,root)
%{_menudir}/tetex-xdvi
%{_iconsdir}/*
%if %{mdkversion} >= 200610
%{_datadir}/applications/*.desktop
%endif

%files -f filelist.dvips dvips
%defattr(-,root,root)

%files -f filelist.dvilj dvilj
%defattr(-,root,root)

%files -f filelist.afm afm
%defattr(-,root,root)

%files -f filelist.doc doc
%defattr(-,root,root)
%docdir %{_datadir}/doc/tetex-doc-%{docversion}
%{_datadir}/doc/tetex-doc-%{docversion}

%files -f filelist.dvipdfm dvipdfm
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/dvipdfpress

%files -f filelist.mfwin mfwin
%defattr(-,root,root)

%files -f filelist.devel devel
%defattr(-,root,root)

%files -f filelist.jadetex -n %{jadename}
%defattr(-,root,root)
%doc %{jadename}-%{jadeversion}/doc/* %{jadename}-%{jadeversion}/ChangeLog

%files -f filelist.xmltex -n %{xmltexname}
%defattr(-,root,root)

%files -f filelist.context context
%defattr(-,root,root)

%files -f filelist.texi2html texi2html
%defattr(-,root,root)

%files usrlocal
%defattr(-,root,root)
%dir /usr/local/share/texmf


