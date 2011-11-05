# revision 24327
# category Package
# catalog-ctan /macros/latex/contrib/mathalfa
# catalog-date 2011-10-19 12:58:31 +0200
# catalog-license lppl1.3
# catalog-version 1.04
Name:		texlive-mathalfa
Version:	1.04
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides means of loading maths alphabets (such as
are normally addressed via macros \mathcal, \mathbb, \mathfrak
and \mathscr), offering various features normally missing in
existing packages for this job.

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
%{_texmfdistdir}/tex/latex/mathalfa/mathalfa.sty
%doc %{_texmfdistdir}/doc/latex/mathalfa/README
%doc %{_texmfdistdir}/doc/latex/mathalfa/mathalfa.pdf
%doc %{_texmfdistdir}/doc/latex/mathalfa/mathalfa.tex
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
