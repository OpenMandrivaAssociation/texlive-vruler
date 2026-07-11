%global tl_name vruler
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3
Release:	%{tl_revision}.1
Summary:	Numbering text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/vruler
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vruler.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vruler.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers facilities for adding a columns of numbering to the
general text so that the text can be properly referenced. The vertical
ruler can be scaled and moved freely. The package may be used either
with LaTeX or with plain TeX.

