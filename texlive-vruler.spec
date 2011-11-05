# revision 21598
# category Package
# catalog-ctan /macros/latex/contrib/vruler
# catalog-date 2011-03-03 10:36:36 +0100
# catalog-license lppl1
# catalog-version 2.3
Name:		texlive-vruler
Version:	2.3
Release:	1
Summary:	Numbering text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/vruler
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vruler.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vruler.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package offers facilities for adding a columns of numbering
to the general text so that the text can be properly
referenced. The vertical ruler can be scaled and moved freely.
The package may be used either with LaTeX or with plain TeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/vruler/vruler.sty
%doc %{_texmfdistdir}/doc/latex/vruler/miscdoc.sty
%doc %{_texmfdistdir}/doc/latex/vruler/vruler-example.tex
%doc %{_texmfdistdir}/doc/latex/vruler/vruler.pdf
%doc %{_texmfdistdir}/doc/latex/vruler/vruler.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
