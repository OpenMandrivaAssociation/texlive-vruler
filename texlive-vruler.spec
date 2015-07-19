# revision 21598
# category Package
# catalog-ctan /macros/latex/contrib/vruler
# catalog-date 2011-03-03 10:36:36 +0100
# catalog-license lppl1
# catalog-version 2.3
Name:		texlive-vruler
Version:	2.3
Release:	10
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.3-2
+ Revision: 757493
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.3-1
+ Revision: 719897
- texlive-vruler
- texlive-vruler
- texlive-vruler

