# revision 27199
# category Package
# catalog-ctan /macros/latex/contrib/mathalfa
# catalog-date 2012-07-16 01:16:42 +0200
# catalog-license lppl1.3
# catalog-version 1.07
Name:		texlive-mathalfa
Version:	1.07
Release:	10
Summary:	General package for loading maths alphabets in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mathalfa
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathalfa.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathalfa.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides means of loading maths alphabets (such as
are normally addressed via macros \mathcal, \mathbb, \mathfrak
and \mathscr), offering various features normally missing in
existing packages for this job.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mathalfa/mathalfa.sty
%doc %{_texmfdistdir}/doc/latex/mathalfa/README
%doc %{_texmfdistdir}/doc/latex/mathalfa/mathalfa.pdf
%doc %{_texmfdistdir}/doc/latex/mathalfa/mathalfa.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
