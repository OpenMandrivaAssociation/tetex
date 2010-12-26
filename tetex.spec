%define bootstrap 0
%{?_without_bootstrap: %global bootstrap 0}
%{?_with_bootstrap: %global bootstrap 1}

%define name            tetex
%define pkgname         tetex
%define version         3.0
%define docversion	3.0
%define pkgversion      3.0
%define tetexversion	3.0
%define tetexrelease    53
%define texmfversion    3.0
%define texmfsrcversion	3.0
%define texmfggversion	3.0n
%define texmfsrcggversion	3.0n
%define jadename	jadetex
%define jadeversion	3.12
%define jaderelease_delta 98
%define jaderelease	%(echo $((%{tetexrelease}+%{jaderelease_delta})))
%define xmltexname	xmltex
%define xmltexversion	1.9
# reset the delta if changing the xmltexversion.
%define xmltexrelease_delta 46
%define xmltexrelease	%(echo $((%{tetexrelease}+%{xmltexrelease_delta})))
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
Release:	%mkrel %{tetexrelease}
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
Source22:	tetex-texi2html-178-images.tar.bz2
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
Patch45:	tetex-3.0-ttf2pk-autoconf.patch
Patch46:	tetex-3.0-CVE-2007-0455.patch
Patch47:	tetex-3.0-CVE-2007-2756.patch
Patch48:	xpdf-3.02-CVE-2007-3387.patch
Patch49:	gd-2.0.33_CVE-2007-3472.patch
Patch50:	gd-2.0.33_CVE-2007-3473.patch
Patch51:	gd-2.0.33_CVE-2007-3474.patch
Patch52:	gd-2.0.33_CVE-2007-3475.patch
Patch53:	gd-2.0.33_CVE-2007-3476.patch
Patch54:	gd-2.0.33_CVE-2007-3477.patch
Patch55:	gd-2.0.33_CVE-2007-3478.patch
Patch57:	tetex-deb-dvips-CVE-2007-5935.patch
Patch58:	t1lib-5.1.0-ub-CVE-2007-4033.patch
Patch59:	tetex-3.0-gentoo-mdv-CVE-2007-5936_5937.patch
Patch60:	tetex-texi2html-178.patch
Patch61:	tetex-3.0-pdftex1405.patch
Patch62:	tetex-3.0-xpdf302pl1.patch
Patch63:	tetex-3.0-xpdf-3.02pl1-CVE-2007-4352_5392_5393.patch
Patch64:	tetex-3.0-getline.patch
Patch65:	tetex-3.0-CVE-2009-1284.diff
Patch66:	tetex-3.0-CVE-2010-0827.diff
Patch67:	tetex-3.0-CVE-2010-0739,1440.diff
Patch68:	tetex-3.0-CVE-2010-0829.diff
Patch69:	tetex-3.0-CVE-2009-3608.diff
Patch70:	tetex-3.0-format_not_a_string_literal_and_no_format_arguments.diff
#
URL:		http://www.tug.org/teTeX/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	tmpwatch
Requires:	dialog
Requires:	ed
Requires:	info-install
Requires:	sam2p
BuildRequires:	autoconf2.1
BuildRequires:	automake1.7
BuildRequires:	libtool
BuildRequires:	bison
BuildRequires:	ed
BuildRequires:	flex
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	lesstif-devel
BuildRequires:	ncurses-devel
BuildRequires:	png-devel
BuildRequires:	gd-devel
BuildRequires:	xpm-devel
BuildRequires:	X11-devel
%if !%bootstrap
%if %{mdkversion} >= 200610
BuildRequires:  desktop-file-utils
%endif
%endif
Obsoletes:	cweb < %{version}-%{release}
Provides:	cweb = %{version}-%{release}
Conflicts:      texlive-texmf
# (Anssi 01/2008) texinfo needs either tetex or texlive-texmf, but it is
# needed during building of texlive, so this provide is here for that:
Provides:	texmf-data = 1

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
Requires:	tetex = %{version}-%{release}
%if %{mdkversion} < 200610
Requires:	tetex-dvips = %{version}-%{release}
%else
Requires:	ghostscript-dvipdf
%endif
Provides:	prosper
Obsoletes:	prosper
Provides:	latex-xcolor
Obsoletes:	latex-xcolor
Provides:	latex-pgf
Obsoletes:	latex-pgf
Obsoletes:      latex-beamer < 0:3.07
Provides:       latex-beamer = 0:3.07

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
Requires:	tetex = %{version}-%{release}
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
Requires:	tetex = %{version}-%{release}

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
Requires:	tetex = %{version}-%{release}

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
Requires:	tetex = %{version}-%{release}

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
Requires:	tetex-xdvi = %{version}-%{release}
BuildArch: noarch
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
Requires:	tetex = %{version}-%{release}
Requires:	tetex-dvips = %{version}-%{release}
Requires:	ghostscript
%if %{mdkversion} >= 200610
Requires:	ghostscript-dvipdf
%endif

%description	dvipdfm
dvidpfm is a DVI to PDF translator for use with TeX.

%package	mfwin
Summary:	Metafont with output window
Group:		Publishing
Requires:	tetex = %{version}-%{release}

%description	mfwin
This package contains METAFONT with window support. Install this
package if you plan to run METAFONT interactively and would like to see
the font building in a output window.

%package	devel
Summary:	Development libraries (kpathsea) for teTeX
Group:		Development/C
Requires:	tetex = %{version}-%{release}

%description	devel
This package contains C headers and libraries, for developing TeX
applications using kpathsea library.

%package -n	%{jadename}
Summary:	TeX macros used by Jade TeX output
Version: 	%{jadeversion}
Release:	%mkrel %{jaderelease}
Group:		Publishing
License: 	Distributable (C) Sebastian Rahtz <s.rahtz@elsevier.co.uk>
URL: 		http://sourceforge.net/projects/jadetex
Requires: 	sgml-common >=  0.6.3-2mdk
Requires: 	tetex = %{tetexversion}-%{mkrel %tetexrelease}
Requires: 	tetex-latex = %{tetexversion}-%{mkrel %tetexrelease}
Requires: 	tetex-dvips = %{tetexversion}-%{mkrel %tetexrelease}
Requires: 	openjade >= 1.3.1

%description -n	%{jadename}
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as TeX files, to obtain DVI, Postscript
or PDF files for example.

%package -n	%{xmltexname}
Summary:	Namespace-aware XML parser written in TeX
Version: 	%{xmltexversion}
Release:	%mkrel %{xmltexrelease}
Group:		Publishing
License: 	LaTeX Project Public License
URL: 		http://www.dcarlisle.demon.co.uk/xmltex/manual.html
Requires: 	tetex = %{tetexversion}-%{mkrel %tetexrelease}
Requires: 	tetex-latex = %{tetexversion}-%{mkrel %tetexrelease}

%description -n	%{xmltexname}
Namespace-aware XML parser written in TeX. This package
also includes passivetex macros, which can be used to process an XML
document which results from an XSL trasformation to formatting objects.

%package	context
Summary:	Document engineering system based on TeX
Version:	%{tetexversion}
Release:	%mkrel %{tetexrelease}
Group:		Publishing
Requires:	tetex = %{version}-%{release}

%description	context
CONTeXT is a document engineering system based on TeX. TeX is a
typesetting system and a program to typeset and produce documents.
CONTeXT is easy to use and enables you to make complex paper and
electronic documents.

%package	texi2html
Summary:	Convert texinfo (GNU docs) directly to HTML for easy reading
Group:		Publishing
License:	GPL
Provides:	texi2html = 1.78
Requires:       tetex = %{version}-%{release}
Conflicts:	tetex < 3.0-48mdv

%description	texi2html
This package converts the GNU standard form of documentation (texinfo) into
HTML files which can be read with any WWW browser.

%package	usrlocal
Summary:	Virtual package for placing local system-wide teTeX files
Group:		Publishing
License:	GPL
Requires:       tetex = %{version}-%{release}

%description	usrlocal
This packages provides just the directory /usr/local/share/texmf
which is defined by the var TEXMFLOCAL in the default config file
and can be used for system-wide teTeX files.

%prep
%setup -q -n %{name}-src-%{tetexversion} -a 7 -a 8 -a 11 -a 20 -a 22
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
cp -p texmf/tex/generic/hyphen/hyphen.tex texmf/tex/generic/hyphen/ushyph1.tex

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

# cvs 20050823
%patch30 -p1 -E
%patch31 -p1 -b .t1auto

# CVE-2007-0104
%patch32 -p1 -b .cve-2007-0104

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

%patch45 -p0 -b .autoconf

pushd libs/gd/
%patch46 -p1 -b .CVE-2007-0455
%patch47 -p0 -b .CVE-2007-2756
%patch49 -p1 -b .cve-2007-3472
%patch50 -p1 -b .cve-2007-3473
%patch51 -p1 -b .cve-2007-3474
%patch52 -p1 -b .cve-2007-3475
%patch53 -p1 -b .cve-2007-3476
%patch54 -p1 -b .cve-2007-3477
%patch55 -p1 -b .cve-2007-3478
popd

pushd libs/xpdf
%patch48 -p1 -b .cve-2007-3387
popd

pushd texk/dvipsk
%patch57 -p0 -b .cve-2007-5935
popd

pushd libs/t1lib
%patch58 -p3 -b .cve-2007-4033
popd

%patch59 -p0 -b .cve-2007-5936_5937

# texi2html 1.78
%patch60 -p1

# pdftex 1.40.5
%patch61 -p1

# xpdf 3.02pl1 (needed by pdftex 1.40.5)
%patch62 -p1

# CVE 2007-4352_5392_5393
%patch63 -p1 -b .cve-2007-4352_5392_5393

%patch64 -p1 -b .getline
%patch65 -p0 -b .CVE-2009-1284
%patch66 -p0 -b .CVE-2010-0827
%patch67 -p0 -b .CVE-2010-0739,1440
%patch68 -p1 -b .CVE-2010-0829
%patch69 -p1 -b .CVE-2009-3608
%patch70 -p1 -b .format_not_a_string_literal_and_no_format_arguments

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
pushd ttf2pk
rm -f configure
aclocal-1.7
autoconf
popd

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
	--with-system-gd \
	--disable-multiplatform \
	--without-dialog \
	--without-texinfo

# (oe) don't use paralell make (%%make) here because the mandriva build system can't handle it properly.
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
pushd ttf2pk
mkdir -p extras/{include,lib}
ln -sf ../../../texk/kpathsea extras/include/kpathsea
ln -sf ../../../texk/kpathsea/.libs/libkpathsea.a extras/lib/libkpathsea.a
rm -f config.cache config.log
./configure --with-kpathsea-dir=./extras
make
popd

# csindex
pushd csindex-%{csidxversion}
make CC="gcc $RPM_OPT_FLAGS"
popd

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
%if %{mdkversion} < 200800 || "%{mdkver}" == "mlcd4"
	    -e "s|^%{_mandir}\(.*\)|%attr(644,root,root) \%{_mandir}\1|" \
%else
	    -e "s|^%{_infodir}\(.*\)|%attr(644,root,root) \%{_infodir}\1.\*|" \
	    -e "s|^%{_mandir}\(.*\)|%attr(644,root,root) \%{_mandir}\1.\*|" \
%endif
		> filelist.full

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

grep -v "/doc/" filelist.full | grep \
	-e xdvi \
	-e "^%attr(644,root,root) %{_mandir}/man1/t1mapper.1" \
	-e "%{_bindir}/t1mapper" | \
	grep -v "%{_datadir}/texmf/tex"		> filelist.xdvi

echo "%{_bindir}/mf" >> filelist.mfwin
echo "%{_bindir}/mfw" >> filelist.mfwin
echo "%{_datadir}/texmf/metafont/config/mf.ini" >> filelist.mfwin

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
	grep -v "%{_datadir}/texmf/fonts/map/dvips/tetex/dvipdfm35.map" |
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

grep -v "/doc" filelist.full | \
	grep -e "^%{_datadir}/texi2html" \
	     -e "^%{_bindir}/texi2html" \
	     -e "^%{_datadir}/texinfo/html/texi2html.html" \
	     -e "^%attr(644,root,root) %{_mandir}/man1/texi2html.1" \
	     -e "^%attr(644,root,root) %{_infodir}/texi2html.info" \
		> filelist.texi2html

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

%if !%bootstrap
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
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-Office-Publishing" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*
%endif
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
%_install_info web2c
%_install_info kpathsea
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :
if [ -e %{texmfconfig}/web2c/updmap.cfg ]; then
	grep -q "^Map bera.map" %{texmfconfig}/web2c/updmap.cfg || %{_bindir}/updmap-sys --quiet --enable Map=bera.map
	%{_bindir}/updmap-sys --quiet
fi

%post latex
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :
%_install_info latex

%post xdvi
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :
%if %mdkversion < 200900
%update_menus
%endif

%post dvips
%_install_info dvips
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%post dvilj
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%post afm
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%post dvipdfm
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%post mfwin
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%post -n %{jadename}
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%post -n %{xmltexname}
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%post context
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%post texi2html
%_install_info texi2html

%post usrlocal
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%postun
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%postun latex
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%postun xdvi
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :
%if %mdkversion < 200900
if [ "$1" = "0" ]; then
%{clean_menus}
fi
%endif

%postun dvips
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%postun dvilj
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%postun afm
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%postun dvipdfm
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%postun mfwin
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%postun -n %{jadename}
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%postun -n %{xmltexname}
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%postun context
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%postun usrlocal
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash >/dev/null || :

%preun
%_remove_install_info %{_infodir}/kpathsea.info.*
%_remove_install_info %{_infodir}/web2c.info.*

%preun dvips
%_remove_install_info %{_infodir}/dvips.info.*

%preun latex
%_remove_install_info %{_infodir}/latex.info.*

%preun texi2html
%_remove_install_info %{_infodir}/texi2html.info.*

%files -f filelist.main
%defattr(-,root,root)
%attr(1777,root,root) %dir %{vartexfonts}
%config %{_sysconfdir}/cron.daily/tetex.cron

%files -f filelist.latex latex
%defattr(-,root,root)

%files -f filelist.xdvi xdvi
%defattr(-,root,root)
%{_iconsdir}/*
%if !%bootstrap
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


%changelog
* Wed May 12 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0-50mdv2010.1
+ Revision: 544580
- P65: security fix for CVE-2009-1284 (debian)
- P66: security fix for CVE-2010-0827 (debian)
- P67: security fix for CVE-2010-0739,1440 (redhat)
- P68: security fix for CVE-2010-0829 (redhat)
- P69: security fix for CVE-2009-3608 (redhat)
- spec file cleanups
- use %%make as it works fine for me...

* Mon Sep 28 2009 Olivier Blin <oblin@mandriva.com> 3.0-49mdv2010.0
+ Revision: 450767
- fix getline() redefinition in ttf2pk as well
- fix getline() redefinition in mpto too
- rediff getline patch, it was not properly applying because of fuzz=3...
- fix duplicate getline() declaration (patch from SM)
- add bootstrap flag to remove desktop-file-util dep
  (from Arnaud Patard)

* Wed Mar 18 2009 Frederik Himpe <fhimpe@mandriva.org> 3.0-48mdv2009.1
+ Revision: 357475
- Define _default_patch_fuzz 3 and Werror_cflags %%nil to make it build
- Move texi2html info file to tetex-texi2html subpackge to fix conflict
  with plain texi2html package

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 3.0-47mdv2009.0
+ Revision: 218426
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Feb 06 2008 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-47mdv2008.1
+ Revision: 162974
- move beamer latex files to avoid overlapping with old ones.
- update unicode package and added missed utf8x.def.
- added translator.sty from beamer package.
- Updated tetex-texmf-extras-gg to release 3.0m:
  o hyperref 6.75g -> 6.77i.
  o beamer 3.06 -> 3.07.
  o pgf 1.01 -> 1.18.
  o pdfsync.sty 1.0 -> 1.1.
  o txfonts.sty 3.2.1: fix \precapapprox and \succapapprox definitions (Young Ryu).
  o pfxfonts.sty 1.1.1: fix \precapapprox and \succapapprox definitions (Young Ryu).
  o txmi|txmi1.tfm|.vf: fix encoding mistakes in Math Italic (Young Ryu).
  o pxmi|pxmi1.tfm|.vf: fix encoding mistakes in Math Italic (Young Ryu).

* Sat Jan 19 2008 Anssi Hannula <anssi@mandriva.org> 3.0-46mdv2008.1
+ Revision: 155107
- provide texmf-data for texinfo

* Fri Jan 18 2008 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-45mdv2008.1
+ Revision: 154904
- Versionize Provides: tetex-texi2html
- Provides: latex-beamer 3.06.

* Thu Jan 17 2008 Anssi Hannula <anssi@mandriva.org> 3.0-44mdv2008.1
+ Revision: 154188
- do not obsolete texi2html

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild now that texlive isn't any more the default
    - drop old menu

* Wed Jan 09 2008 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-43mdv2008.1
+ Revision: 147344
- Bump release and rebuild as was not uploaded correctly in cooker.

* Wed Jan 09 2008 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-42mdv2008.1
+ Revision: 147127
- Rebuild.

* Wed Jan 09 2008 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-41mdv2008.1
+ Revision: 147123
- Disable parallel building (as there are problems building in klodia).
- Bump release number due to Marcelo fixes to the Emi bot.

* Mon Jan 07 2008 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-40mdv2008.1
+ Revision: 146199
+ rebuild (emptylog)

* Sun Jan 06 2008 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-39mdv2008.1
+ Revision: 146101
- fix %%{_infodir} and %%{_mandir} in filelists.
- Patch60: update texi2html to release 1.78 (and texi2html shouldn't be duplicated as a standalone external package), fix bug #35003.
- Patch57: security fix for CVE-2007-5935 (dvips), merged from Vincent Danen updates.
- Patch58: security fix for CVE-2007-4033 (embedded t1lib), merged from Vincent Danen updates
- Patch59: security fix for CVE-2007-{5936,5937} (embedded gd), merged from Vincent Danen updates.
- Patch61: update pdfTeX to release 1.40.5.
- Patch62: update internal xpdf libs to 3.02pl1 (needed by pdfTeX 1.40.5).
- Patch63: security fix for CVE-2007-{4352,5392,5393} (embedded xpdf 3.02pl1), merged from Vincent Danen updates for xpdf 3.02.
- Updated tetex-texmf-extras-gg to release 3.0l:
  o hyperref 6.75t -> 6.77g.
  o oberdiek 2007/01/24 -> 2007/10/01.
  o url.sty 3.2 -> 3.3.
  o framed.sty 0.8a -> 0.95.
  o graphics/pdftex.def 0.04d -> 0.04i.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - use std info-install macros
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel
    - fix summary-ended-with-dot

* Sun Sep 09 2007 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-38mdv2008.0
+ Revision: 83954
- move dvipdfm35.map to dvips subpackage not to dvipdfm.

* Sun Sep 09 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 3.0-37mdv2008.0
+ Revision: 83284
- Really fix xmltex and jadetex Requires.

* Sun Sep 09 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 3.0-36mdv2008.0
+ Revision: 83283
- Quick fix for breakage of Requires in jadetex/xmltex and all
  subpackages below them introduced in last commit (note that jadetex
  and xmltex redefine version and release).

* Sat Sep 08 2007 David Walluck <walluck@mandriva.org> 3.0-35mdv2008.0
+ Revision: 82540
- remove references to %%{PACKAGE_VERSION} and replace with %%{version}-%%{release}
- version cweb Provides/Obsoletes
- make sure every subpackage at least requires tetex = %%{version}-%%{release}
- make sure every subpackage requires on %%{version}-%%{release} and not something like >= 1.0.7-52mdk (should fix bug #33323)
- %%exclude %%{_datadir}/texmf/fonts/map/dvips/tetex/dvipdfm35.map in dvips to fix file conflict with other subpackage

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Sat Aug 25 2007 Pascal Terjan <pterjan@mandriva.org> 3.0-34mdv2008.0
+ Revision: 71190
- Fix mkrel usage
- Add patches 49-55 for CVE-2007-347[2-8] and CVE-2007-3387 (#32278)
- Don't build in subshell (aka see the errors)
- Add P46 for CVE-2007-0455 (#30989)
- Add P47 for CVE-2007-2756 (#31389)
- Use mkrel

* Sat Aug 25 2007 Pascal Terjan <pterjan@mandriva.org> 3.0-32mdv2008.0
+ Revision: 71147
- Fix build issues (autoconf, libtool, missing ushyph1.tex)
- Fix for lzma manpages/info

  + David Walluck <walluck@mandriva.org>
    - Conflicts: texlive-texmf
    - set relsuffix for mdv2008.0 (why don't we use %%mkrel?)


* Thu Mar 15 2007 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-31mdv2007.0
+ Revision: 144390
- Bumped triggers to 3.0-31mdv2007.1 accordingly.
- Added tetex-xdvi to Requires for tetex-doc subpackage.

* Sun Mar 11 2007 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-29mdv2007.1
+ Revision: 141160
- Rebuild because tetex-doc RPM was unsigned.
- Updated tetex-texmf-extras-gg to release 3.0k:
  o hyperref 6.75r -> 6.75t.
  o oberdiek 2007/01/24 -> 2007/03/07.

* Wed Mar 07 2007 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-28mdv2007.1
+ Revision: 134300
- Use trigger migration for Latin Modern for any tetex release < 3.0-28mdv2007.1 (thanks to Camille).

* Wed Feb 28 2007 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-27mdv2007.1
+ Revision: 127332
- Rebuild for fixing bug #29000.

* Tue Feb 20 2007 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-26mdv2007.1
+ Revision: 123111
- Updated tetex-texmf-extras-gg to release 3.0j:
  o removed duplicate url.sty (David Walluck).

* Sun Feb 18 2007 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-25mdv2007.1
+ Revision: 122235
- fixed tetex-xdvi %%post scripts.

* Sat Feb 17 2007 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-24mdv2007.1
+ Revision: 122201
- Backported patches from pdftex 1.40.3 (Patch39) fixing:
  o document which used type 1 and truetype or opentype fonts.
    resulted in broken pdfs (729).
  o maplines starting with = would not work as advertised.
  o xpdf would complain that PDF 1.7 is too new.
- Install missed pdftosrc (Patch40).
- Added Patch41 for kpathsea for showing warnings when a
  .cnf file is not found.
- Added Patch42 for fixing typos in cwebman.tex, and updating
  cwebmac.tex to release 3.67 (previous 3.64).
- Move /usr/local/share/texmf into a standalone subpackage
  (fix bug #21018).
- Added Patch43 for CVE-2007-0650.
- Merged Patch44 from Fedora (don't inherit incorrect permission for
  ls-R).
- Updated tetex-texmf-extras-gg to release 3.0i:
  o latex/graphics/pdftex.def 0.03t -> 0.04d.
  o added tex/generic/pdftex/glyphtounicode.tex v1.1.
  o plain/tex/base/cwebmac.tex 3.64 -> 3.67.
  o hyperref 6.75r -> 6.75q.
  o footmisc 5.3c -> 5.3d.
- merged Gwenole fix for %%relsuffix to SPEC file.

* Sun Jan 28 2007 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-23mdv2007.0
+ Revision: 114626
- Updated tetex-texmf-extras-gg to release 3.0h:
        o hyperref 6.75o -> 6.75q.
        o xcolor 2.09 -> 2.11.
        o preview 2004-04-11 -> 2006-08-25.
        o oberdiek 20060826 -> 20070124.
- fixed fmtutil.cnf for texi2dvi (thanks to Gwenole).
- fixed xdvizilla (patch from Guillaume Rousse, bug #22698).
- Dropped dependencies to X11R6-contrib (bug #22698)
- removed BuildRequires: tetex-context from package
  tetex-latex (close bug #22413).
- reworked Patch36.
- use version 3.0g also for %%texmfsrcggversion.

* Mon Jan 22 2007 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-22mdv2007.1
+ Revision: 111677
- Reworked Patch36
- fixed SPEC file.
- Remove %%elseif (not supported).
- bump version number to 22mdv2007.1.
- move updmaps from tetex-dvips to main packages (needed also by pdftex).
- updated pdfTeX engine to release 1.40.1 (Patch36 & Patch37).
- updated Patch30 (bug #26479).
- added powerdot (bug #27713), probably still needed fourier-GUT.
- Added Patch33 (sprintf was not passing right number of arguments).
- Added Patch34 to fix some man pages.
- added simpdftex script from TeXLive (Patch35).
- Updated tetex-texmf-extras-gg to release 3.0g:
        - hyperref 6.75d -> 6.75o.
        - powerdot (bug #27713), probably needs fourier-GUT.
        - fixed syst-etex.tex for pdfTeX 1.40.1.
        - movie15 2007/01/17.

* Fri Jan 19 2007 Andreas Hasenack <andreas@mandriva.com> 3.0-21mdv2007.1
+ Revision: 110844
- force 2007.1 release tag for now (see #28256). This still has to be properly
  fixed
- fix patch filename

  + Giuseppe Ghib√≤ <ghibo@mandriva.com>
    - P32: security fix for CVE-2007-0104 (embedded xpdf), from
      Stew Benedict.

* Tue Jan 16 2007 Giuseppe Ghib√≤ <ghibo@mandriva.com> 3.0-20mdv2007.0
+ Revision: 109662
- added Patch31 for building with autoconf-2.5.60.
- better trigger for updmap Latin Modern map migration (bug #25639).
- remove obsolete Latin Modern map and enc files.
- force updmap-sys call in %%post to have fontmap updated in case of
  customized updmap.cfg (for bug #25639).

  + Oden Eriksson <oeriksson@mandriva.com>
    - Import tetex

* Thu Sep 07 2006 Giuseppe GhibÚ <ghibo@mandriva.com> 3.0-18mdv2007.0
- Updated tetex-texmf-extras-gg to release 3.0f:
	- beamer 3.01 -> 3.06.
	- pgf -> 1.01.

* Wed Sep 06 2006 Giuseppe GhibÚ <ghibo@mandriva.com> 3.0-17mdv2007.0
- Updated Patch20 (dvipsgeneric).
- Added ghostscript-dvipdf to tetex-latex's Requires (fix bug #23627).
- Merged fixes/changes from tetex's cvs 20050823 and TeXLive (updates dvips
  to release 5.95b, pdftex to 1.30.6, xdvik to release 22.8.10,
  web2c to 7.5.5), and merged security fixes from Stew Benedict:
  - security fix for CAN-2004-0941 (internal gd)
  - security fix for CVE-2006-2906 (internal gd)
- Updated internal dvipng to release 1.8,
- Updated internal xpdf to 3.0.1pl2 (and merged security fixes). Bug #23405.
- Updated tetex-texmf-extras-gg to release 3.0e:
	- pdfpages.sty 0.3e -> 0.4a.
        - fixed utf8raw.tex.
        - xcolor 2.00 -> 2.09.
	- hyperref 6.74m -> 6.75d.
	- latex -> 2005/12/01.
	- tools -> 2005/12/01 (from latex 2005/12/01)).
	- graphics.sty 1.0n -> 1.0o (from latex 2005/12/01).
	- cyrillic -> 2005/12/01 (from latex 2005/12/01).
	- psnfss 9.2 -> 9.2a (from latex 2005/12/01).
	- caption 3.0c -> 3.0j.
	- lm font (Latin Modern) 0.92 -> 1.0.
	- babel.sty 3.8d -> 3.8h.
	- thumbpdf.sty 3.7 -> 3.8.
	- url.sty 3.1 -> 3.2.
	- optional.sty 2.2 -> 2.2b.
	- oberdiek -> 20060826.
	- marvosym -> 2.1.
	- xkeyval 2.0 -> 2.5e.
	- pstricks -> 2006.
	- metapost docs -> 0.9.
- XDG menus.

* Fri May 05 2006 Giuseppe GhibÚ <ghibo@mandriva.com> 3.0-16mdk
- Merged security updates from Stew Benedict <sbenedict@mandriva.com>:
  security update for CVE-2005-3191,3192,3193 (Patch30),
  security update for overflows in goo/gmem.c (Patch31),
  additional overflow issues discovered by Chris Evans (Patch32)
  (CVE-2005-3624,3625,3626,3627,3628).
- added automake1.7 to BuildRequires.

* Fri Jan 27 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 3.0-15mdk
- patch29: generate a local libtool script for ttf2mk

* Mon Jan 23 2006 Till Kamppeter <till@mandriva.com> 3.0-14mdk
- Added "Requires: ghostscript ghostscript-dvipdf" to the
  tetex-dvipdfm package. This way it is assured that the dvipdf tools
  work, and there is also the simple command "dvipdf" (without "m",
  "t", or "press") available.

* Sun Sep 18 2005 Giuseppe GhibÚ <ghibo@mandriva.com> 3.0-13mdk
- use www-browser instead of mozilla in tetexdoc (fix bug #18653).

* Wed Sep 07 2005 Giuseppe GhibÚ <ghibo@mandriva.com> 3.0-12mdk
- Provides|Obsoletes: latex-xcolor, latex-pgf (fix bug #14734)
- Updated tetex-texmf-extras-gg to release 3.0d:
	- ha-prosper 4.21.
	- ppr-prv 0.13c.
	- talk 1.0.1.

* Wed Sep 07 2005 Gˆtz Waschk <waschk@mandriva.org> 3.0-11mdk
- fix bug 18163

* Thu Sep 01 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 3.0-10mdk
- build kpathsea.a objects with pic (needed for evince shared libs)

* Fri Jul 22 2005 Giuseppe GhibÚ <ghibo@mandriva.com> 3.0-9mdk
- Updated tetex-texmf-extras-gg to release 3.0c:
	- algorithmic.sty 2005/07/05.
	- put back mtplus support in my{1,2,3}mtt.fd.
	- envlab 1.2.

* Sat Mar 12 2005 Giuseppe GhibÚ <ghibo@mandrakesoft.com> 3.0-8mdk
- updated tetex-texmf-extras-gg to release 3.0a (fix for bug #14885).

* Thu Mar 10 2005 Giuseppe GhibÚ <ghibo@mandrakesoft.com> 3.0-7mdk
- Updated Patch11 (badscript), merged from RH.
- Removed Patch7 (2.0.2-texconfig-mf).
- Updated Patch21 for calling www-browser instead of netscape.
- Added Patch17, partially backported patch from CAN-2005-0206
  (bug #13754).
- Removed Patch29 (badc).

* Thu Feb 17 2005 Giuseppe GhibÚ <ghibo@mandrakesoft.com> 3.0-6mdk
- Added sam2p to Requires (for fixing bug #13723).

* Wed Feb 16 2005 Giuseppe GhibÚ <ghibo@mandrakesoft.com> 3.0-5mdk
- Clean initial /var/lib/texmf (fix bug #13691).

* Mon Feb 14 2005 Giuseppe GhibÚ <ghibo@mandrakesoft.com> 3.0-4mdk
- Modified Patch1 to use 'pdfetex' engine instead of 'tex' also for hugelatex.
- Fixed missed jadetex .fmt files (Camille).
- Set TEXMF env var before makeinstall (avoid conflicts with installed tetex).

* Sat Feb 12 2005 Giuseppe GhibÚ <ghibo@mandrakesoft.com> 3.0-3mdk
- Updated tetex-texmf-extras-gg to release 3.0a (removed unneded cyrillic/*.fdd files).
- Used pdfetex as default latex engine in fmtutil.cnf (Thomas request).
- removed "context" files from tetex-latex package (Thierry).

* Fri Feb 11 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.0-2mdk
- fix ttf2pk build ex-nihilo (i.e. sans tetex-devel installed beforehand)

* Thu Feb 10 2005 Giuseppe GhibÚ <ghibo@mandrakesoft.com> 3.0-1mdk
- Rebuilt Patch0, 1, 3, 4, 5, 6, 10, 12.
- Removed Patch8 (xdvik).
- Removed Patch28 (typefacename), merged upstream.
- Removed texi2html 1.64 Sources (mainstream contains texi2html 1.76).
- Added Patch for CAN-2004-0888, CAN-2005-0064 (Jindrich Novy).
- Updated tetex-texmf-extras-gg to release 3.0 (and removed files merged upstream).

* Thu Aug 26 2004 Giuseppe GhibÚ <ghibo@mandrakesoft.com> 2.0.2-19mdk
- Added support for czech makeindex (csindex).
- texmfgg archive updated to release 2.0.2e:
	- psnfss 9.1b
	- cyrillic: 2004-01-26.
	- tools: 2004-02-27.
	- LaTeX base Issue 16: 2003/12/01.
	- babel: 2004-02-20.
	- changebar: 3.4d -> 3.4g.
	- amsthm.sty (amslatex): 2000/10/26 v2.08 -> 2004/08/06 v2.20.
	- upref.sty (amslatex): 1.12d -> 2.01.
	- amsmidx.sty: 2.01.
	- amsart.cls (amslatex): 2.08 -> 2.20.
	- amsbook.cls (amslatex): 2.01 -> 2.20.
	- amsdtx.cls (amslatex): 2.02 -> 2.06.
	- amsproc.cls (amslatex): 2.08 -> 2.20.
	- amsldoc.cls (amslatex): 2.02 -> 2.06.
	- amsrefs.sty (amslatex): 1.23 -> 2.0.
	- ifoption.sty (amslatex): 1.01 -> 1.02.
	- matscinet.sty (amslatex): 1.02 -> 2.01.
	- pcatcode.sty (amslatex): 1.03 -> 1.04.
	- rkeyval.sty (amslatex): 2.00 -> 1.05.
	- textcmds.sty (amslatex): 1.03 -> 1.05.
	- algorithm.sty.
	- SIstyle.sty: 2.0.

* Sun Jun 20 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.0.2-18mdk
- re-add BuildRequires: ed.

* Wed Jun 16 2004 Per ÿyvind Karlsen <peroyvind@linux-mandrake.com> 2.0.2-17mdk
- fix buildrequires.

* Sat Jun 05 2004 <lmontel@n2.mandrakesoft.com> 2.0.2-16mdk
- Rebuild-

* Wed Apr 28 2004 Giuseppe GhibÚ <ghibo@mandrakesoft.com> 2.0.2-15mdk
- Rebuilt against latest gettext 0.14.1.

