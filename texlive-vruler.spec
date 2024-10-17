Name:		texlive-vruler
Version:	21598
Release:	2
Summary:	Numbering text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/vruler
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vruler.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vruler.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers facilities for adding a columns of numbering
to the general text so that the text can be properly
referenced. The vertical ruler can be scaled and moved freely.
The package may be used either with LaTeX or with plain TeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/vruler/vruler.sty
%doc %{_texmfdistdir}/doc/latex/vruler/miscdoc.sty
%doc %{_texmfdistdir}/doc/latex/vruler/vruler-example.tex
%doc %{_texmfdistdir}/doc/latex/vruler/vruler.pdf
%doc %{_texmfdistdir}/doc/latex/vruler/vruler.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
